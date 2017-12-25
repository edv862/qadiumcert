from django.conf.urls import url

from .views import *

urlpatterns = [
    url(
        r'certificates/$',
        ListCreateCertificateView.as_view(),
        name='cert-lc'
    ),
    url(
        r'certificates/(?P<pk>[0-9]*)/$',
        RetrieveUpdateDestroyCertificateView.as_view(),
        name='cert-rud'
    ),
    url(
        r'ip-address/$',
        ListCreateIPView.as_view(),
        name='ip-lc'
    ),
    url(
        r'ip-address/(?P<pk>[0-9]*)/$',
        RetrieveUpdateDestroyIPView.as_view(),
        name='ip-rud'
    ),
]
