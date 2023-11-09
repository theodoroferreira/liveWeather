from django.db import models


class RealTimeData(models.Model):
    data_field_1 = models.CharField(max_length=255)
    data_field_2 = models.IntegerField()
