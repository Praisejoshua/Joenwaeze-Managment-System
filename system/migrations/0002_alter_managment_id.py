# Generated by Django 5.1 on 2024-09-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
