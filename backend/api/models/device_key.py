from django.db import models
from encrypted_model_fields.fields import EncryptedCharField


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
    app_key = EncryptedCharField(max_length=100)
    claimed_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=UNCLAIMED,
    )
    organization = models.ForeignKey('api.Organization', models.DO_NOTHING, blank=True, null=True)