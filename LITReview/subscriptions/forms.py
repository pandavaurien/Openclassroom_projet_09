from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import UserFollows


class SubscriptionsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']
        labels = {"followed_user": ""}
        widgets = {'followed_user': forms.TextInput()}


