from django import forms
from .models import *

class scholarForm(forms.ModelForm):
    class Meta:
        model = Scholar
        fields = ('firstName','lastName')

class workingForm(forms.ModelForm):
    class Meta:
        model = Working
        fields = '__all__'

class bankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'

class scholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = '__all__'  

class subsidizedForm(forms.ModelForm):
    class Meta:
        model = Subsidized
        fields = '__all__'

class percentileForm(forms.ModelForm):
    class Meta:
        model = Percentile
        fields = '__all__' 

class nonWorkingForm(forms.ModelForm):
    class Meta:
        model = NonWorking
        fields = '__all__'     