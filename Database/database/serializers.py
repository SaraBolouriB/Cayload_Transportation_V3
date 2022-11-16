from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'

    def create(self, valide_data):
        return Site.objects.create(**valide_data)

class ServiceSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Service
        fields = '__all__'

    def create(self, valide_data):
        return Service.objects.create(**valide_data)

class BlockchainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blockchian
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = '__all__'

# CONNECTION ---------------------------------------------------------
class SiteServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteService
        fields = '__all__'

class SiteBlockchainSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteBlockhain
        fields = '__all__'

class SiteLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteLogin
        fields = '__all__'