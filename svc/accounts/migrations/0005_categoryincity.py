# Generated by Django 3.0.10 on 2021-02-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210214_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryInCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CategoryList')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.CityList')),
            ],
        ),
    ]
