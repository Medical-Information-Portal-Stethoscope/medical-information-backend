# Generated by Django 4.2.2 on 2023-07-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(
                choices=[
                    ('user', 'user'),
                    ('doctor', 'doctor'),
                    ('moderator', 'moderator'),
                    ('admin', 'admin'),
                ],
                default='user',
                max_length=50,
                verbose_name='role',
            ),
        ),
    ]
