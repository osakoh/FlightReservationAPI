# Generated by Django 3.2 on 2021-04-13 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightAPP', '0003_auto_20210413_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='flightAPP.flight'),
        ),
    ]
