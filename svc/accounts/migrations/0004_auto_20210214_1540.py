# Generated by Django 3.0.10 on 2021-02-14 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210213_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('IsActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CountryId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.CountryList')),
            ],
        ),
        migrations.CreateModel(
            name='AddressList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Street', models.CharField(blank=True, max_length=500, null=True)),
                ('ZipCode', models.CharField(blank=True, max_length=50, null=True)),
                ('AddedDate', models.DateField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CityId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.CityList')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='citylist',
            name='StateId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.StateList'),
        ),
    ]
