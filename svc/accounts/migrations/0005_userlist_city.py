# Generated by Django 3.0.10 on 2021-02-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210212_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='City',
            field=models.CharField(default='Kolkata', max_length=30),
        ),
    ]
