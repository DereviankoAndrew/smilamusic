from django.shortcuts import render, redirect

from .models import StudentsAmount, PhoneNumbers
from .forms import StudentRequestForm
# Create your views here.

def index(request):

    form = StudentRequestForm()
    students_amount = StudentsAmount.objects.first()
    number = PhoneNumbers.objects.first()

    if request.method == 'POST':
        form = StudentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'smilaMusicSite/thank-for-request.html', {

            })

    return render(request, 'smilaMusicSite/index.html', {
        'students_amount': students_amount,
        'number': number,
        'form': form,

    })

