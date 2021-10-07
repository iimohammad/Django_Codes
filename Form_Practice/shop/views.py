from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonalInformation
from .models import Person
from django.http import HttpResponse
from django.shortcuts import render
def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)


def submit_person(request):
    if request.method == 'GET':
        form = PersonalInformation()
        return render(request, 'new_person.html',{'form':form})
    elif request.method == 'POST':
        form = PersonalInformation(request.POST)
        message = "Error"
        
        if form.is_valid():
            person=Person() 
            person.gender = form.cleaned_data['gender']
            person.full_name = form.cleaned_data['full_name']
            person.height = form.cleaned_data['height']
            person.age = form.cleaned_data['age']
            person.save()
            return HttpResponse(person,status=201)
        return HttpResponse(message,status=400)
