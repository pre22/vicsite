# Generated by Django 4.0.3 on 2022-03-10 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_coin_coinaddress_balance_and_more'),
        ('investments', '0003_auto_20220310_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='balance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.balance'),
        ),
    ]
