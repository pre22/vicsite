# Generated by Django 4.0.3 on 2022-03-09 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useraccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coinaddress',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccounts.coin'),
        ),
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]