# Generated by Django 4.0.3 on 2022-03-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentstatus',
            name='invest_status',
            field=models.CharField(choices=[('A', 'Active'), ('N', 'Unactive')], max_length=20),
        ),
    ]
