from django import forms
from .models import hotel_hoteldetails, staffmanagement
from django import forms
from django.forms import ModelForm

class hoteldetailsform(forms.ModelForm):
    class Meta:
        model = hotel_hoteldetails
        fields = '__all__'

class hotelstaffmanagement(forms.ModelForm):
    class Meta:
        model = staffmanagement
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = staffmanagement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'SELECT'

