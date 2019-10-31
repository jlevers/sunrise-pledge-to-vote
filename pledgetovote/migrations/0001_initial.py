# Generated by Django 2.2.6 on 2019-10-31 04:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zipcode', localflavor.us.models.USZipCodeField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.CharField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator])),
                ('picture', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pledgetovote.Address')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pledgetovote.Location')),
            ],
        ),
    ]
