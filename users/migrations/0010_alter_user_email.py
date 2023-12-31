# Generated by Django 4.2.3 on 2023-08-16 14:45

import django.core.validators
from django.db import migrations, models

import users.validators


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0009_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(
                error_messages={'unique': 'A user with that username already exists!'},
                max_length=50,
                unique=True,
                validators=[
                    django.core.validators.EmailValidator(),
                    users.validators.RestrictedEmailValidator(),
                ],
            ),
        ),
    ]
