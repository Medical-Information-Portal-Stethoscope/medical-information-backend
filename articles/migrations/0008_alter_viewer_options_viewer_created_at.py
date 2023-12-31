# Generated by Django 4.2.3 on 2023-08-09 11:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0007_remove_article_views_count_viewer_article_viewers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewer',
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'viewer',
                'verbose_name_plural': 'viewers',
            },
        ),
        migrations.AddField(
            model_name='viewer',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name='created_at',
            ),
            preserve_default=False,
        ),
    ]
