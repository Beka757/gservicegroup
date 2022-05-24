from django import forms


class ServiceImportForm(forms.Form):
    excel_file = forms.FileField(required=True)


class FilterForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    category = forms.CharField(max_length=100, required=False)
    mark = forms.CharField(max_length=100, required=False)