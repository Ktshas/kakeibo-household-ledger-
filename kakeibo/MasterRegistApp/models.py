from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class AccountList(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=30)
    bank = models.CharField(max_length=20, null=True)
    account_num = models.IntegerField(null=True, validators=[MaxValueValidator(999999999999)])
    account_kind = models.IntegerField(null=True, validators=[MaxValueValidator(99)])
    account_kind_other = models.CharField(null=True, max_length=20)
    account_purpose = models.IntegerField(null=True, validators=[MaxValueValidator(99)])
    account_purpose_other = models.CharField(null=True, max_length=30)
    account_balance = models.BigIntegerField(default=0)
    
    class Meta:
        db_table = 'AccountList'