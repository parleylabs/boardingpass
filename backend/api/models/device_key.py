from django.db import models


class DeviceKey(models.Model):
    CLAIMED = 'claimed'
    UNCLAIMED = 'unclaimed'
    STATUS_CHOICES = [
        (CLAIMED, 'Claimed'),
        (UNCLAIMED, 'Unclaimed'),
    ]
    device_key_id = models.AutoField(primary_key=True)
    dev_eui = models.CharField(max_length=75, unique=True)
    app_eui = models.CharField(max_length=75)
    app_key = models.CharField(max_length=75)
    claimed_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=UNCLAIMED,
    )
    owner = models.ForeignKey('api.User', models.DO_NOTHING, blank=True, null=True)