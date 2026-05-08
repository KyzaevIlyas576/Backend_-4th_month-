from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def company_list_view(request):
    if request.method == 'GET':
        companies = forms.Company.objects.all().order_by('-id')
    return render(request, 'tour_crud/company_list.html', {'companies': companies})


def create_company_view(request):
    if request.method == 'POST':
        form = forms.CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/company_list/')
    else:
        form = forms.CompanyForm()
    return render(request, 'tour_crud/company_form.html', {'form': form})


def delete_company_view(request, id):
    company_id = get_object_or_404(models.Company, id=id)
    if request.method == 'POST':
        company_id.delete()
        return redirect('/company_list/')


def update_company_view(request, id):
    company_id = get_object_or_404(models.Company, id=id)
    if request.method == 'POST':
        form = forms.CompanyForm(request.POST, instance=company_id)
        if form.is_valid():
            form.save()
            return redirect('/company_list/')
    else:
        form = forms.CompanyForm(instance=company_id)
    return render(request, 'tour_crud/company_form.html', {
        'form': form,
        'company_id' : company_id,
        })


# Create your views here.