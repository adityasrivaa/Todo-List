from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .form import *
from .models import *

from django.contrib.auth.hashers import check_password,make_password



def home(request):
            form = TodoForm()
            todos =Todo.objects.all().order_by('priority')
            return render(request,"home.html", context={'form': form, 'todos': todos})

def sign_up(request):
    if request.method == 'POST':
        f_name= request.POST.get('fname')
        l_name= request.POST.get('lname')
        email= request.POST.get('email')
        password= request.POST.get('pwd')
        mobile= request.POST.get('mbl')
        gender= request.POST.get('gender')


        reg_obj = Registration(
            first_name= f_name,
            last_name= l_name,
            email= email,
            password= make_password(password),
            mobile=mobile,
            gender=gender
        )


        reg_obj.save()


        return redirect('home')
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        try:
            email_id= Registration.objects.get(email=email)
            if check_password(password,email_id.password):
                request.session['name'] = email_id.first_name
                return redirect('home')
            else:
                return HttpResponse("Wrong Password")

        except:
            return HttpResponse("Wrong email")
        

def logout(request):
    request.session.clear()
    return redirect('home')


def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            return render(request,"home.html", context={'form': form})
        

def delete_todo(request, id):
    Todo.objects.get(pk = id).delete()
    return redirect('home')


def change_todo(request, id, status):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')