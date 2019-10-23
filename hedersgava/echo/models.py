from django.db import models

# Create your models here.

UNIT = [
    ('Temperature Sensor', '°C'),
    ('Voltage Meter', 'V'),
    ('Current Meter', 'A'),
    ('Power Meter', 'W'),
]


class Record(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    record_time = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.id)


class Data(models.Model):
    record = models.ForeignKey(
        'Record',
        on_delete=models.CASCADE,
    )
    device = models.CharField(max_length=100)
    value = models.FloatField()
    unit = models.CharField(
        max_length=25,
        choices=UNIT,
        default='Temperature Sensor',
    )
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.record.id, self.id)
