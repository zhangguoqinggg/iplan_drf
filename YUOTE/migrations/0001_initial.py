# Generated by Django 2.2.5 on 2020-03-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('industy_type', models.IntegerField(choices=[(1, '汽车'), (2, '快消')], verbose_name='客户类型')),
            ],
        ),
    ]
