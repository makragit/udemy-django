from django.shortcuts import render
#from first_project.models import Topic,Webpage,AccessRecord
from .models import Topic,Webpage,AccessRecord,temp_User
from . import forms

from .forms import NewUserForm
from first_app.forms import UserForm, UserProfileInfoForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    #my_dict = {'insert_me':"Hello I am from views.py !!"}

    context_dict = {'text': 'hello world', 'number': 100}

    #return render(request, 'first_app/index1.html', context=date_dict)
    return render(request, 'first_app/index.html', context=context_dict)



def help(request):
    help_dict = {'insert_help': 'help help help'}
    return render(request, 'first_app/help.html', context=help_dict)

def users(request):
    users_list = temp_User.objects.order_by('f_name')
    users_dict = {'users_dict': users_list}
    return render(request, 'first_app/users.html', context=users_dict)

def form(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])


    return render(request, 'first_app/form.html', {'form':form})

def users(request):
    users_list = temp_User.objects.order_by('f_name')
    #users_dict = {'users_dict': users_list}

    form = NewUserForm

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")

    return render(request,'first_app/users.html', {'form':form, 'users_dict':users_list})

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/url_template.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print("TESTESTS")
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html',
                  {'user_form': user_form,
                   'profile_form':profile_form,
                   'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login")
    else:
        return render(request, 'first_app/login.html', {})

