from django.db import models


# model to store the rate of basic uses
class BasicUsageRate(models.Model):
    percent =  models.FloatField()
    minimum =  models.FloatField()
    maximum =  models.FloatField()
 
    def __str__(self):
        return '{} %'.format(self.percent)


# model to store the ranges of added costs for the association
class PartnershipCostRange(models.Model):
    cost =  models.FloatField()
    minimum =  models.FloatField()
    maximum =  models.FloatField()
 
    def __str__(self):
        return 'cost {} ({} - {})'.format(self.cost, self.minimum, self.maximum)


# model to store the variables to be based on the calculations
class BiddingVariable(models.Model):
    is_active = models.BooleanField(default=False)
    basicusagerate = models.ForeignKey(BasicUsageRate, on_delete=models.CASCADE)
    sellercommission = models.FloatField()
    fixedstoragerate = models.FloatField()
    partnershipcostranges = models.ManyToManyField(PartnershipCostRange)

    def __str__(self):
        return '{}'.format(self.pk)


# model to store bid calculations
class BiddingCalculation(models.Model):
    amount = models.FloatField()
    biddingvariables = models.ForeignKey(BiddingVariable, on_delete=models.CASCADE)
    calculationdate = models.DateField()

    def __str__(self):
        return '{}  -  {}'.format(self.pk, self.amount)