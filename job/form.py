from django import forms
from .models import Application, Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'cover_letter']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        # fields = ['title', 'job_type', 'description', 'description', 'vacancy', 'salary', 'category', 'experience']
