# Generated by Django 3.1.1 on 2020-10-09 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0004_auto_20201007_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
