# Generated by Django 3.1.5 on 2021-01-30 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockchainpart', '0003_auto_20210130_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='chain',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blockchainpart.chain'),
        ),
    ]
