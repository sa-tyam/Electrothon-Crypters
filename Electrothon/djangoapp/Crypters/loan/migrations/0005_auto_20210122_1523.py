# Generated by Django 3.0.3 on 2021-01-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_auto_20210122_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='issue_date',
            field=models.DateField(auto_now=True),
        ),
    ]