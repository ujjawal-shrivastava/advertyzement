import graphene
from graphene_django import DjangoObjectType
from core.models import Banks, BankBranches

class BankType(DjangoObjectType):
    class Meta:
        model = Banks
        fields = ("id", "name")

class BankBranchType(DjangoObjectType):
    bank = graphene.Field(BankType)

    class Meta:
        model = BankBranches
        fields = ("ifsc", "bank_id", "branch", "address", "city", "district", "state", "bank_name")

    def resolve_bank(self, info):
        return self.bank
    
# All banks List Type
bankList = graphene.List(BankType, search=graphene.String(), first=graphene.Int(), skip=graphene.Int())

# All Branches List Type
branchesList = graphene.List(BankBranchType, search=graphene.String(), first=graphene.Int(), skip=graphene.Int())