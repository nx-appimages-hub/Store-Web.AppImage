# Generated by Django 2.2 on 2020-04-07 18:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_auto_20200407_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='hash',
        ),
        migrations.AddField(
            model_name='packageversion',
            name='hash',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]