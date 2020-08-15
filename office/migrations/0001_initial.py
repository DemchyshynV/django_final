# Generated by Django 3.1 on 2020-08-15 15:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^([0])(\\d{9})$', 'not valid phone number')])),
                ('price', models.IntegerField()),
                ('users', models.ManyToManyField(related_name='offices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'office',
            },
        ),
    ]