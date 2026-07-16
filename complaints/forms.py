from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'phone', 'complaint_type', 'subject', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }