from django.db import models
import requests


class AccountInfo(models.Model):
    account_name = models.CharField(max_length=50, null=False, blank=False)
    account_summ = models.IntegerField()

    def __str__(self):
        return f'{self.account_name} - {self.account_summ}'

    def delete_everything(self):
        AccountInfo.objects.all().delete()
