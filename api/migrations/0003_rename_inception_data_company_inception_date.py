# Generated by Django 4.1.1 on 2022-09-17 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_team_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='inception_data',
            new_name='inception_date',
        ),
    ]
