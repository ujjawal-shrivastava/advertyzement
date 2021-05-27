import graphene
from .types import bankList, branchesList
from .resolvers import resolve_banks, resolve_bank_branches

class Query(graphene.ObjectType):
    
    banks = bankList
    bank_branches = branchesList

    def resolve_banks(*args, **kwargs):
        return resolve_banks(*args,**kwargs)

    def resolve_bank_branches(*args, **kwargs):
        return resolve_bank_branches(*args, **kwargs)


schema = graphene.Schema(query=Query)