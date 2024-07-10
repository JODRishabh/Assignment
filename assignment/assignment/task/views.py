from django.shortcuts import render, redirect
from .forms import CustomerForm
from datetime import datetime

# Create your views here.
def home(request):
    # form = CustomerForm()
    if request.method == "POST":
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm
        current_datetime = datetime.now
    context={'form':form, 'current_datetime':current_datetime}
    return render(request,'home.html',context)