# Generated by Django 4.0.1 on 2022-08-09 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('return', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='return',
            options={'ordering': ['-id']},
        ),
    ]
