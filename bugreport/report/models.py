from django.db import models
import uuid


class Parts(models.Model):
    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Primary_key True'

    part_id = models.UUIDField(verbose_name='PartID', primary_key=True, unique=True, default=uuid.uuid4, max_length=40)
    part_name = models.CharField(verbose_name='PartName', unique=False, default=1, max_length=40, blank=True, null=True)

    def __str__(self):
        return self.part_name


class TestPart(models.Model):
    class Meta:
        verbose_name_plural = 'Primary_key False'

    part_id = models.UUIDField(verbose_name='PartID', primary_key=False, unique=True, default=uuid.uuid4, max_length=40)
    part_name = models.CharField(verbose_name='PartName', unique=False, default=1, max_length=40, blank=True, null=True)

    def __str__(self):
        return self.part_name
