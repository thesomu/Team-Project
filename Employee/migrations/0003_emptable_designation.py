# Generated by Django 3.2.3 on 2021-05-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_emptable_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='emptable',
            name='designation',
            field=models.CharField(default='null', max_length=30),
        ),
    ]