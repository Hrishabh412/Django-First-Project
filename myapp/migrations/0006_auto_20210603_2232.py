# Generated by Django 3.1.7 on 2021-06-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='name',
            field=models.IntegerField(default=0),
        ),
    ]
