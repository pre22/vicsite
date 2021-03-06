# Generated by Django 4.0.3 on 2022-03-13 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WithdrawStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "withdraw_status",
                    models.CharField(
                        choices=[("P", "Pending"), ("F", "Failed"), ("C", "Completed")],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Withdraw",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wallet_address", models.CharField(max_length=500)),
                ("amount", models.CharField(max_length=100, null=True)),
                (
                    "balance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.balance",
                    ),
                ),
                (
                    "coin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.coinaddress",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        choices=[("P", "Pending"), ("F", "Failed"), ("C", "Completed")],
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.withdrawstatus",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TransactionHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sn", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InvestmentStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "invest_status",
                    models.CharField(
                        choices=[("A", "Active"), ("N", "Unactive")], max_length=20
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DepositStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "deposit_status",
                    models.CharField(
                        choices=[("P", "Pending"), ("F", "Failed"), ("C", "Completed")],
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deposit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.CharField(max_length=50)),
                ("proof", models.ImageField(upload_to="")),
                ("transaction_date", models.DateTimeField(auto_now_add=True)),
                (
                    "coin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.coin"
                    ),
                ),
                (
                    "company_wallet_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.coinaddress",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        choices=[("P", "Pending"), ("F", "Failed"), ("C", "Completed")],
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.depositstatus",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
