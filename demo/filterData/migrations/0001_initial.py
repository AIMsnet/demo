# Generated by Django 3.1.1 on 2020-10-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=225)),
                ('emob', models.CharField(max_length=10)),
                ('eadd', models.CharField(max_length=225)),
                ('pin', models.CharField(max_length=6)),
                ('edept', models.CharField(max_length=125)),
            ],
        ),
    ]
