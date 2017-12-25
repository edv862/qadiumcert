from django.conf.urls import url

from .views import *

urlpatterns = [
    url(
        r'certificate/create/$',
        CertificateCreateView.as_view(),
        name='certificate-create',
    ),
    url(
        r'certificate/list/$',
        CertificatesListView.as_view(),
        name='certificate-list'
    ),
    url(
        r'ip-address/create/$',
        IpAddressCreateView.as_view(),
        name='ip-address-create',
    ),
    url(
        r'ip-address/list/$',
        IpAddressListView.as_view(),
        name='ip-address-list',
    ),
]
