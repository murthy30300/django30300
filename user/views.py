from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.template.backends import django

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.

from user.forms import ContactForm
from django.shortcuts import render
from hotel.models import hotel_hoteldetails
from django.contrib.auth.models import User

from .forms import profileform


# Create your views here.
def test(request):
    return render(request, 'user/test.html')


def userviewhotel(request):
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('userviewhotel')
    else:
        form = profileform()

    return render(request, 'user/userviewprofile.html', {'form': form})




def userhome(request):
    return render(request, 'user/userhomepage.html')


def userviewprofile(request):

    return render(request, 'user/userviewprofile.html', )


def useraddemail(request):
    if request.method == "POST":
        email = request.POST.get('emailu')
        cuser = request.user
        cuser.email = email
        cuser.save()
        return render(request, 'user/userviewprofile.html')


def useraddfirstname(request):
    if request.method == "POST":
        email = request.POST.get('firstnameu')
        cuser = request.user
        print(cuser.email)
        cuser.first_name = email
        cuser.save()
        return render(request, 'user/userviewprofile.html')


def useraddlastname(request):
    if request.method == "POST":
        email = request.POST.get('lastnameu')
        cuser = request.user
        print(cuser.email)
        cuser.last_name = email
        cuser.save()
        return render(request, 'user/userviewprofile.html')


def projecthomepage(request):
    return render(request, 'user/projecthomepage.html')


def adminhomepage(request):
    return render(request, 'admin/adminhomepage.html')


def managerhomepage(request):
    return render(request, 'hotel/managerhomepage.html')


def staffhomepage(request):
    return render(request, 'hotel/staffhomepage.html')


def userhomepage(request):
    return render(request, 'user/userhomepage.html')


def Contact(request):
    form = ContactForm(request.POST or None)  # Create form instance with POST data or None
    if request.method == 'POST':
        if form.is_valid():  # Check if form is valid
            subject = 'Thank you for sending your query'
            message = 'we will be very grateful to assist you,\n our support agents will get back you too very soon'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Mail sent successfully')
            return redirect('Contact')
    else:
        form = ContactForm()  # Create an empty form instance for GET request
    return render(request, 'user/Contact.html', {'form': form})


def About(request):
    return render(request, 'user/About.html')


def signinup(request):
    return render(request, 'user/signinup.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'user/signinup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
            if len(username) > 5:
                return render(request, 'user/projecthomepage.html')
            else:
                return render(request, 'hotel/hotelhomepage.html')
        else:
            messages.info(request, 'Password do not match')
    return render(request, 'user/signinup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username) > 5:
                return render(request, 'user/projecthomepage.html')
            else:
                return render(request, 'hotel/hotelhomepage.html')
        else:
            messages.info(request, 'Invalid username or password.')
            return render(request, 'user/signinup.html')
    else:
        return render(request, 'user/signinup.html')



def logout(request):
    auth.logout(request)
    return redirect('signinup')


def search_view(request):
    if request.method == 'GET':
        hotellocation = request.GET.get('location')
        results = hotel_hoteldetails.objects.filter(hotellocation__icontains=hotellocation)
        return render(request, 'user/userviewhotel.html', {'hotels': results})
    else:
        return render(request, 'user/error.html')



