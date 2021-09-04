# Generated by Django 3.2.6 on 2021-09-04 07:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(verbose_name='age')),
                ('phone_number', models.PositiveBigIntegerField(unique=True, validators=[django.core.validators.RegexValidator('^(\\+98|0)?9\\d{9}$', message='Invalid phone number')], verbose_name='phone number')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email')),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'profile',
            },
        ),
    ]