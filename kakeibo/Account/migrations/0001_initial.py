# Generated by Django 2.2.7 on 2019-11-07 23:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountList',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=30)),
                ('bank', models.CharField(max_length=20, null=True)),
                ('account_num', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(999999999999)])),
                ('account_kind', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('account_kind_other', models.CharField(max_length=20, null=True)),
                ('account_purpose', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99)])),
                ('account_purpose_other', models.CharField(max_length=30, null=True)),
                ('account_balance', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'AccountList',
            },
        ),
    ]
