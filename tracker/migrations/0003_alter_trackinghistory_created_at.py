# Generated by Django 5.0.6 on 2024-07-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_requestlogs_alter_trackinghistory_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackinghistory',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
