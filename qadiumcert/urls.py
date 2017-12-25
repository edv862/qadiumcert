from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(
        r'^admin/',
        admin.site.urls
    ),
    url(
        r'^api/',
        include(
            'certificates.api_urls',
            namespace='api'
        )
    ),
    url(
        r'^',
        include(
            'certificates.urls',
            namespace='main'
        )
    ),
]
