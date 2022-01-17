from django.shortcuts import render, redirect
from .models import Name
from .forms import NameForm


def home(request):
    names = Name.objects.all()
    form = NameForm()
    hey = Name.objects.all()
    context = {
        'form': form,
        'names': names,
        'hey': hey,

    }
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'hellopeople/home.html', context,)


def people(request):
    names = Name.objects.all()
    return render(request, 'hellopeople/people.html', {'title': 'Люди', 'names': names})
