from django.conf import settings
from django.db import models
from accounts.models import Balance

INVEST_STATUS = (
    ("A", "Active"),
    ("N", "Unactive"),
)

class Package(models.Model):
    name = models.CharField(max_length=30, null=True)
    maximum_stake = models.PositiveIntegerField(default="000000", null=True)
    minimum_stake = models.PositiveIntegerField(default="000.00", null=True)
    roi = models.PositiveIntegerField()
    duration = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    


class Investment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    sn = models.PositiveIntegerField(null=True)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default="000.00", null=True)
    status = models.CharField(max_length=20, choices=INVEST_STATUS)

    def __str__(self):
        return "{} {}".format(self.user.firstname, self.user.lastname)
    
