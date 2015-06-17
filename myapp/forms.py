#-*- coding:utf-8 -*-

from django import forms
from django.contrib import admin
from myapp.models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ['name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    exclude = ['age']
    form = PersonForm