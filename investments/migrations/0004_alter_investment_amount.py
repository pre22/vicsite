# Generated by Django 4.0.3 on 2022-03-21 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0003_alter_package_maximum_stake_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='amount',
            field=models.PositiveIntegerField(default='000.00', null=True),
        ),
    ]