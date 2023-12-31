# Generated by Django 4.2.3 on 2023-08-09 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0008_alter_viewer_options_viewer_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewer',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='viewers',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
