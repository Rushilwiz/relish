from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Response

class ResponseForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'post'
    helper.form_action = ''

    helper.add_input(Submit('submit', 'submit'))

    class Meta:
        model = Response
        fields = ['name', 'email', 'phone', 'address']
