import datetime

from django.db import models
from django.utils import timezone

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


class Contract(models.Model):
    contract_label  = models.CharField(max_length=256, default="Hauptzähler")
    contract_number = models.CharField(max_length=256)
    
class Invoice(models.Model):
    invoice_number      = models.IntegerField("Rechnungsnummer", default=0)
    file_name           = models.CharField("Rechnungsname", max_length=256, default="")
    creation_date       = models.DateField("Rechnungsdatum", default=datetime.date.today)
    payment_target_date = models.DateField("Zahlbar bis", blank=True, null=True)
    cancellation_date   = models.DateField("Storniert am", blank=True, null=True)
    period_start        = models.DateField("Abrechnungsperiode von", default=datetime.date.today().replace(day=1))
    period_end          = models.DateField("Abrechnungsperiode bis", default=last_day_of_month(datetime.date.today()))
    counter_start       = models.FloatField("Zählerstartwert", blank=True, null=True)
    counter_end         = models.FloatField("Zählerendwert", default=0)
    net_sum             = models.DecimalField("Rechnungsbetrag (Netto)", max_digits=12, decimal_places=4, default=0)
    billed              = models.DateField("Abgerechnet am", blank=True, null=True, default=None)
    contract            = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True)
    invoice_update      = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    draft               = models.BooleanField("Entwurf", default=False)