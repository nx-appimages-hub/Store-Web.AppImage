# Generated by Django 2.2 on 2020-04-12 21:55

import apps.package.model.package
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0008_auto_20200412_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]