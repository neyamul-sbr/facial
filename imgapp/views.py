from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.db.models.query import QuerySet


def upload_img(request):
    if request.method == 'POST':
        form = ImageUpForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            usr = CapTable(

                name = name,
                age = age,
            )
            usr.save()
            return redirect('result')
            
    else:
        form = ImageUpForm()
    return render(request, 'imgapp/cc1.html', {'form':form})

def result(request):
    query_results = CapTable.objects.all()
    context = {
        'query_results': query_results
    }
    return render(request, 'imgapp/cc2.html', context )
    




