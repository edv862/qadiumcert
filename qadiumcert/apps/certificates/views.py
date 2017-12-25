# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .models import Certificate, IpAddress
from .serializers import CertificateSerializer, IpAddressSerializer
from .forms import CertificateForm, IpAddressForm


# REST API functions.
class ListCreateCertificateView(ListCreateAPIView):
    model = Certificate
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()


class RetrieveUpdateDestroyCertificateView(
    RetrieveUpdateDestroyAPIView
):
    model = Certificate
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()


class ListCreateIPView(ListCreateAPIView):
    model = IpAddress
    serializer_class = IpAddressSerializer
    queryset = IpAddress.objects.all()


class RetrieveUpdateDestroyIPView(
    RetrieveUpdateDestroyAPIView
):
    model = IpAddress
    serializer_class = IpAddressSerializer
    queryset = IpAddress.objects.all()


# Template views.
class CertificatesListView(ListView):
    model = Certificate
    queryset = Certificate.objects.all()
    template_name = 'certificate-list.html'
    context_object_name = 'certificates'


class CertificateCreateView(CreateView):
    model = Certificate
    queryset = Certificate.objects.all()
    form_class = CertificateForm
    template_name = 'certificate-create-form.html'
    success_url = reverse_lazy('certificates:list')


class IpAddressListView(ListView):
    model = IpAddress
    queryset = IpAddress.objects.all()
    template_name = 'certificate-list.html'
    context_object_name = 'certificates'


class IpAddressCreateView(CreateView):
    model = IpAddress
    queryset = IpAddress.objects.all()
    form_class = IpAddressForm
    template_name = 'certificate-create-form.html'
    success_url = reverse_lazy('certificates:list')
