# Generated by Django 3.1.6 on 2021-02-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20210205_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_professional',
            field=models.BooleanField(default=False),
        ),
    ]