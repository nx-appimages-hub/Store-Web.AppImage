# Generated by Django 2.2.28 on 2023-01-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0020_package_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='download',
            field=models.TextField(blank=True, null=True),
        ),
    ]
