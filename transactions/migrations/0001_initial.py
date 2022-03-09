# Generated by Django 4.0.3 on 2022-03-09 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_status', models.CharField(choices=[('P', 'Pending'), ('F', 'Failed'), ('C', 'Completed')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invest_status', models.CharField(choices=[('A', 'Active'), ('N', 'Unactive')], default='A', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdraw_status', models.CharField(choices=[('P', 'Pending'), ('F', 'Failed'), ('C', 'Completed')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]