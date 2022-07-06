from django.db import models

# Create your models here.

class BasicUsageRate(models.Model):
    percent =  models.FloatField()
    minimum =  models.FloatField()
    maximum =  models.FloatField()
 
    def __str__(self):
        return '{} %'.format(self.percent)

class PartnershipCostRange(models.Model):
    cost =  models.FloatField()
    minimum =  models.FloatField()
    maximum =  models.FloatField()
 
    def __str__(self):
        return '{} - {}'.format(self.minimum, self.maximum)

class BiddingVariable(models.Model):
    is_active = models.BooleanField(default=False)
    basicusagerate = models.ForeignKey(BasicUsageRate, on_delete=models.CASCADE)
    sellercommission = models.FloatField()
    fixedstoragerate = models.FloatField()
    partnershipcostranges = models.ManyToManyField(PartnershipCostRange)

    def __str__(self):
        return '{}'.format(self.pk)


class BiddingCalculation(models.Model):
    amount = models.FloatField()
    biddingvariables = models.ForeignKey(BiddingVariable, on_delete=models.CASCADE)
    calculationdate = models.DateField()

    def __str__(self):
        return '{}  -  {}'.format(self.pk, self.amount)