# Generated by Django 3.0.3 on 2021-01-21 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('not defined', 'not defined')], max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('user_type', models.CharField(choices=[('farmer', 'farmer'), ('shopkeeper', 'shopkeeper')], max_length=200)),
                ('mobile_number', models.CharField(max_length=13)),
                ('additional_mobile_number', models.CharField(max_length=13, null=True)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pin_code', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
