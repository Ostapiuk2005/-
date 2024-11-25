# Generated by Django 5.1.1 on 2024-11-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=4)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]