from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['msg']
            return render(request, 'base.html')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form':form})

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, "students.html", {'form':form})

def sample(request):
    if request.method == 'POST':
        name = request.POST.get('nmm')
        age = request.POST.get('ag')
        place = request.POST.get('pll')
        course = request.POST.get('cs')
        st = Student(name=name, age=age, place=place, course=course)
        st.save()
        return redirect('home')
    else:
        return render(request, "sample.html")
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()

            f_name = form.cleaned_data.get('first_name')
            l_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            pro = Profile(user=user, f_name=f_name, l_name=l_name, email=email, username=username)
            pro.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {'form':form})

def Userlogn(request):
    if request.method == 'POST':
        form = UserloginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserloginForm()
    return render(request, "login.html", {'form':form})

def uslogout(request):
    logout(request)
    return redirect('base')

def items(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('itmlist')
    else:
        form = ItemForm()
    return render(request, "items.html", {'form':form})

def itmlist(request):
    itm = Items.objects.all()
    return render(request, "itemlist.html", {'item':itm} )

def delt(request,pk):
    item = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect(itmlist)

def editt(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('itmlist')
    else:
        form = ItemForm(instance=item)
    return render(request, "update.html", {'form':form})

