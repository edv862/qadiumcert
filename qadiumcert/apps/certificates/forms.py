from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

from .models import Certificate, IpAddress


class CertificateForm(forms.ModelForm):
    expires = forms.DateTimeField(
        widget=DateTimePicker(
            options={"format": "DD/MM/YYYY HH:mm:ss"}
        )
    )

    class Meta:
        model = Certificate
        fields = '__all__'


class IpAddressForm(forms.ModelForm):
    class Meta:
        model = IpAddress
        fields = '__all__'
