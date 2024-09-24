from django import forms
from .models import Managment

class ManagementForm(forms.ModelForm):
    class Meta:
        model = Managment
        fields = ['seller_name', 
                  'Weight', 
                  'amount', 
                  'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Use date input type
        }
