# Generated by Django 3.0.10 on 2021-02-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210212_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiclist',
            name='ForceCloseReason',
            field=models.CharField(max_length=3999, null=True),
        ),
    ]
