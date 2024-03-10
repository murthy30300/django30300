from django import forms
from django import forms
from .models import hoteldetails, UserProfile


class ContactForm(forms.Form):
    email = forms.EmailField()


class hoteldetailsform(forms.ModelForm):
    class Meta:
        model = hoteldetails
        fields = '__all__'

class profileform(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'