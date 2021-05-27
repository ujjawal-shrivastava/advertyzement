from django.contrib import admin
from .models import Banks, Branches, BankBranches

# Register your models here.
admin.site.register(Banks)
admin.site.register(Branches)
admin.site.register(BankBranches)
