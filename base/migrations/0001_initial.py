# Generated by Django 4.0.3 on 2022-05-14 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resturant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('location', mapbox_location_field.models.LocationField(blank=True, map_attrs={}, null=True)),
                ('logo', models.ImageField(blank=True, default='', null=True, upload_to='logos')),
                ('bio', models.TextField(blank=True, null=True)),
                ('is_delivery', models.BooleanField(blank=True, default=False, null=True)),
                ('is_wallet', models.BooleanField(blank=True, default=False, null=True)),
                ('is_promo_code', models.BooleanField(blank=True, default=False, null=True)),
                ('discount', models.FloatField(blank=True, default=0.0, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, default='', null=True, upload_to='avatars')),
                ('description', models.TextField(blank=True, null=True)),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('is_driver', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]