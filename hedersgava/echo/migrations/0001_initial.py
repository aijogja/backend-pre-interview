# Generated by Django 2.2.6 on 2019-10-23 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('record_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('unit', models.CharField(choices=[('Temperature Sensor', '°C'), ('Voltage Meter', 'V'), ('Current Meter', 'A'), ('Power Meter', 'W')], default='Temperature Sensor', max_length=25)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echo.Record')),
            ],
        ),
    ]
