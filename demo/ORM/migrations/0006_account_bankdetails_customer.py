# Generated by Django 3.1.1 on 2020-10-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0005_auto_20201009_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atype', models.CharField(max_length=100)),
                ('accNo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobno', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.CharField(max_length=6)),
                ('account', models.ManyToManyField(to='ORM.Account')),
                ('customer', models.ManyToManyField(to='ORM.Customer')),
            ],
        ),
    ]
