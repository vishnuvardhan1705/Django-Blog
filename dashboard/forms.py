from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blogs.models import Blog,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'