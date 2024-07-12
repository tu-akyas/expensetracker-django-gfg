# Generated by Django 5.0.6 on 2024-07-11 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('request_info', models.TextField()),
                ('request_type', models.CharField(max_length=100)),
                ('request_method', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='trackinghistory',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
