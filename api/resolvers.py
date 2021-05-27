from core.models import Banks, BankBranches
from django.db.models.query_utils import Q
from django.contrib.postgres.search import SearchQuery, SearchVector

# Resolver for Banks Query
def resolve_banks(root, info, search=None, first=None, skip=None):
        qs = Banks.objects.all()

        if search:
            qs = qs.filter(Q(name__icontains=search))
        
        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs

# Resolver for Bank Branches Query
def resolve_bank_branches(root, info, search=None, first=None, skip=None):
        qs = BankBranches.objects.all()

        #Full Text Search Implemetation
        if search:
            qs = qs.annotate(search=SearchVector("ifsc", "bank_name",
                                                 "branch", "address", "city", "district", "state", config='english')).filter(search=SearchQuery(search))

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs