from django.db import models


class Banks(models.Model):
    name = models.CharField(max_length=49, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        verbose_name = "bank"
        db_table = 'banks'

    def __str__(self) -> str:
        return self.name


class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank = models.ForeignKey(Banks, models.CASCADE, blank=True, null=True)
    branch = models.CharField(max_length=74, blank=True, null=True)
    address = models.CharField(max_length=195, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        verbose_name = "branch"
        verbose_name_plural = "branches"
        db_table = 'branches'

    def __str__(self) -> str:
        return f'{self.branch} ({self.bank.name})'


class BankBranches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank_id = models.BigIntegerField(blank=True, null=True)
    branch = models.CharField(max_length=74, blank=True, null=True)
    address = models.CharField(max_length=195, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=26, blank=True, null=True)
    bank_name = models.CharField(max_length=49, blank=True, null=True)

    class Meta:
        verbose_name = "bank branch"
        verbose_name_plural = "bank branches"
        managed = False  # Created from a view. Don't remove.
        db_table = 'bank_branches'

    def __str__(self) -> str:
        return f'{self.branch} ({self.bank_name})'
