# Generated by Django 3.0.10 on 2021-02-17 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210212_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('cost', models.IntegerField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.TopicList')),
            ],
        ),
    ]
