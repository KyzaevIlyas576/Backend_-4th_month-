from django.shortcuts import render
from django.db.models import Avg
from . import models


def company_list(request):
    companies = models.Company.objects.all()

    for company in companies:
        company.avg_rating = company.reviews.aggregate(avg=Avg('rating'))['avg']

    return render(request, 'company_list.html', {'companies': companies})


# Create your views here.
