# Generated by Django 3.1.6 on 2021-02-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20210205_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='side',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]