from django.shortcuts import render
from django.shortcuts import get_object_or_404
from jsonview.decorators import json_view
from jsonview.exceptions import BadRequest
from django import forms
from .models import RinggoldRecord

def home(request):
    return render(request, 'ringgold/index.html')

class GetRecordForm(forms.Form):
    ringgold_id = forms.IntegerField()

@json_view
def get_record(request):
    f = GetRecordForm(request.GET)
    if not f.is_valid():
        raise BadRequest('Invalid ringgold_id')
    r = get_object_or_404(RinggoldRecord, ringgold_id=f.cleaned_data['ringgold_id'])
    return r.to_orcid_json()
