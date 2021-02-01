from django.db import models
from hashlib import sha256
import datetime
from django.urls import reverse
from .utils import SymmetricEncryption, JsonApi, EncryptionApi
import pytz

import json
from flask import Flask , jsonify
from django.contrib.auth.models import User


class Block(models.Model):
    time_stamp = models.DateTimeField(auto_now=True)
    index = models.IntegerField(auto_created=True, blank=True)
    ammount_transferred = models.IntegerField(blank=True, null=True)
    remaining_balance = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=255, blank=True)
    previous_hash = models.CharField(max_length=255)
    chain = models.ForeignKey(to='Chain', on_delete=models.CASCADE, null=True, blank=True)
    nonce = models.CharField(max_length=255, default=0, blank=True)

    def __str__(self):
        return "Block " + str(self.index) + " on " + self.chain.user.username

    def __repr__(self):
        return '{}: {}'.format(self.index, str(self.hash)[:6])

    def __hash__(self):
        return sha256(
            u'{}{}{}{}'.format(
                self.index,
                self.ammount_transferred,
                self.remaining_balance,
                self.previous_hash,
                self.nonce).encode('utf-8')).hexdigest()

    @staticmethod
    def generate_next(latest_block, ammount_transferred, remaining_balance):
        block = Block(
            ammount_transferred=ammount_transferred,
            remaining_balance=remaining_balance,
            index=latest_block.index + 1,
            time_stamp=datetime.datetime.now(tz=pytz.utc),
            previous_hash=latest_block.hash,
            nonce=SymmetricEncryption.generate_salt(26),
        )
        block.nonce = SymmetricEncryption.generate_salt(26)
        while not block.valid_hash():
            block.nonce = SymmetricEncryption.generate_salt(26)
        block.hash = block.__hash__()

        block.save()                # todo: remove

        return block

    def is_valid_block(self, previous_block):
        if self.index != previous_block.index + 1:
            log.warning('%s: Invalid index: %s and %s' % (self.index, self.index, previous_block.index))
            return False
        if self.previous_hash != previous_block.hash:
            log.warning('%s: Invalid previous hash: %s and %s' % (self.index, self.hash, previous_block.hash))
            return False

        if self.__hash__() != self.hash and self.index > 1:
            log.warning('%s: Invalid hash of content: %s and %s' % (self.index, self.hash, self.__hash__()))
            return False
        if not self.valid_hash() and self.index > 1:
            log.warning('%s: Invalid hash value: %s' % (self.index, self.hash))
            return False
        return True

    def valid_hash(self):
        """simulate Proof of work"""
        return True

class Chain(models.Model):
    """
    allows for multiple blockchain entities to exist simultaneously
    """
    time_stamp = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def __len__(self):
        return self.block_set.count()

    def __repr__(self):
        return '{}: {}'.format(self.user.username, self.last_block)

    @property
    def last_block(self):
        return self.block_set.order_by('index').last()

    def create_seed(self, ammount_transferred, remaining_balance):
        assert self.pk is not None
        seed = Block.generate_next(
            Block(hash=sha256('seed'.encode('utf-8')).hexdigest(),
                  index=-1),
            ammount_transferred=ammount_transferred,
            remaining_balance=remaining_balance
        )
        seed.chain = self
        seed.save()

    def is_valid_next_block(self, block):
        return block.is_valid_block(self.last_block)

    def add(self, ammount_transferred, remaining_balance):
        if not self.block_set.count():
            self.create_seed(ammount_transferred = ammount_transferred, remaining_balance = remaining_balance)

        block = Block.generate_next(
            self.last_block,
            ammount_transferred = ammount_transferred,
            remaining_balance = remaining_balance
        )
        block.chain = self
        block.save()
        return block

    def is_valid_chain(self, blocks=None):
        blocks = blocks or list(self.block_set.order_by('index'))
        if not len(blocks):
            log.warning('Empty chain')
            return False
        if len(blocks) == 1 and blocks[0].index != 0:
            log.warning('Missing seed block in chain.')
            return False
        if not all(pblock.index + 1 == block.index == required_index
                   for pblock, block, required_index in zip(blocks[:-1], blocks[1:], range(1, len(blocks)))):
            log.warning('Chain is not sequential')
            return False
        return all(block.is_valid_block(pblock)
                   for pblock, block in zip(blocks[:-1], blocks[1:]))

    def replace_chain(self, new_chain):
        if self.is_valid_chain(new_chain) and len(new_chain) > len(self):
            self.block_set.all().delete()
            for block in new_chain:
                block.chain = self
                block.save()
