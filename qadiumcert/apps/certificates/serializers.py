from rest_framework.serializers import ModelSerializer

from .models import Certificate, IpAddress, Usage


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class IpAddressSerializer(ModelSerializer):
    certificate = CertificateSerializer(
        many=True,
    )

    class Meta:
        model = IpAddress
        fields = ('address', 'owner', 'certificate')


class UsageSerializer(ModelSerializer):
    class Meta:
        model = Usage
        fields = '__all__'
