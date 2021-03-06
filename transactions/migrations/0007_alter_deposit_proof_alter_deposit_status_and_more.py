# Generated by Django 4.0.3 on 2022-03-23 14:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_withdraw_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='proof',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Failed', 'Failed'), ('Completed', 'Completed')], default='status', max_length=20),
        ),
        migrations.AlterField(
            model_name='depositstatus',
            name='deposit_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Failed', 'Failed'), ('Completed', 'Completed')], max_length=20),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='status',
            field=models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('INSUFFICIENT', 'INSUFFICIENT'), ('FAILURE', 'FAILURE')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawstatus',
            name='withdraw_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Failed', 'Failed'), ('Completed', 'Completed')], max_length=20),
        ),
    ]
