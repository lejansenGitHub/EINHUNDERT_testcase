# Generated by Django 3.2.4 on 2021-07-01 12:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_label', models.CharField(default='Hauptzähler', max_length=256)),
                ('contract_number', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(default=0, verbose_name='Rechnungsnummer')),
                ('file_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Rechnungsname')),
                ('creation_date', models.DateField(default=datetime.date.today, verbose_name='Rechnungsdatum')),
                ('payment_target_date', models.DateField(blank=True, null=True, verbose_name='Zahlbar bis')),
                ('cancellation_date', models.DateField(blank=True, null=True, verbose_name='Storniert am')),
                ('period_start', models.DateField(default=datetime.date.today, verbose_name='Abrechnungsperiode von')),
                ('period_end', models.DateField(default=datetime.date.today, verbose_name='Abrechnungsperiode bis')),
                ('counter_start', models.FloatField(blank=True, null=True, verbose_name='Zählerstartwert')),
                ('counter_end', models.FloatField(default=0, verbose_name='Zählerendwert')),
                ('net_sum', models.DecimalField(decimal_places=4, default=0, max_digits=12, verbose_name='Rechnungsbetrag (Netto)')),
                ('billed', models.DateField(blank=True, default=None, null=True, verbose_name='Abgerechnet am')),
                ('draft', models.BooleanField(default=False, verbose_name='Entwurf')),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.contract')),
                ('invoice_update', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.invoice')),
            ],
        ),
    ]