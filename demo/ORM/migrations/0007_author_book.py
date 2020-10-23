# Generated by Django 3.1.1 on 2020-10-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0006_account_bankdetails_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generType', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(to='ORM.Author')),
            ],
        ),
    ]
