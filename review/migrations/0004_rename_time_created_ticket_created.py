# Generated by Django 5.2.3 on 2025-06-29 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_rename_time_created_review_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='time_created',
            new_name='created',
        ),
    ]
