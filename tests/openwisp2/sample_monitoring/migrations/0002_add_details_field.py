# Generated by Django 3.0.3 on 2020-05-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='details',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='metric',
            name='details',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='threshold',
            name='details',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
