# Generated by Django 3.2.3 on 2021-05-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exportProduct_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=20)),
                ('price_per_piece', models.FloatField()),
                ('date_of_export', models.DateField()),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Client_Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('client_name', models.CharField(max_length=20)),
                ('client_country', models.CharField(max_length=20)),
                ('quantity_demanded', models.IntegerField()),
                ('product_name', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.DO_NOTHING, to='Export.export')),
            ],
        ),
    ]
