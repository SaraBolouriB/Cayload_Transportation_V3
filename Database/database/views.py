from .models import *
from .serializers import *

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

import yagmail
import random
import string

INVALID_DATA = status.HTTP_400_BAD_REQUEST
INCOMPLETE_DATA = status.HTTP_400_BAD_REQUEST
SUCCEEDED_REQUEST = status.HTTP_200_OK
CREATED = status.HTTP_201_CREATED
DELETED = status.HTTP_204_NO_CONTENT
NOT_FOUND = status.HTTP_404_NOT_FOUND

class SiteView(viewsets.ViewSet):
    
    def create(self, request):
        site_data = request.data
        data = SiteSerializer(data=site_data)

        if data.is_valid():
            data.save()
            return Response("Done", status=CREATED)
        else:
            return Response(data.errors, status=INVALID_DATA)

    def list(self, request):
        sites = Site.objects.all()
        sites_ser = SiteSerializer(sites, many=True)
        sitesName = []
        for site in sites_ser.data:
            sitesName.append(site['siteName'])
        return Response(data=sitesName, status=SUCCEEDED_REQUEST)

    def destroy(self, request, pk=None):
        site = Site.objects.filter(id=pk)
        if site.exists():
            site.delete()
            return Response("Done", status=SUCCEEDED_REQUEST)
        else:
            return Response("No Item", status=NOT_FOUND)

class ServiceView(viewsets.ViewSet):
    
    def create(self, request):
        service_data = request.data
        site_id = service_data.pop('site_id')
              
        data = ServiceSerializer(data=service_data)
        if data.is_valid():
            data.save()
        else:
            return Response(data.errors, status=INVALID_DATA)

        service_id = Service.objects.get(name=service_data['name']).id
        data_collection = {
            'site': site_id,
            'service' : service_id
        }
        
        siteService = SiteServiceSerializer(data=data_collection)
        if siteService.is_valid():
            siteService.save()
            return Response("Done", status=SUCCEEDED_REQUEST)
        else:
            return Response(siteService.errors, status=INVALID_DATA)
        
    def partial_update(self, request, pk=None):
        service = Service.objects.get(id=pk)
        updated_service = ServiceSerializer(service, data=request.data, partial=True)
        if updated_service.is_valid():
            updated_service.save()
            return Response('Done', status=SUCCEEDED_REQUEST)
        else:
            return Response(updated_service.errors, status=INVALID_DATA)

    def list(self, request, site_id=None):
        _services = SiteService.objects.all().filter(site_id=site_id)
        service_objs = []
        if _services.exists():
            for service in _services.values():
                service_objs.append(Service.objects.filter(id=service['service_id']).values()[0])
        
        return Response(service_objs, status=SUCCEEDED_REQUEST)

    def destroy(self, request, pk=None):
        service = Service.objects.filter(id=pk)
        if service.exists():
            service.delete()
            return Response("Done", status=SUCCEEDED_REQUEST)
        else:
            return Response("No Item", status=NOT_FOUND)

class BlockchainView(viewsets.ViewSet):
    
    def create(self, request):
        blockchain_data = request.data
        
        
        data = BlockchainSerializer(data=blockchain_data)
        # site_id = blockchain_data.pop('site_id')
        if data.is_valid():            
            data.save()         
        else:
            return Response(data.errors, status=INVALID_DATA)
        
        blockchain_id = Blockchian.objects.get(url=blockchain_data['url'], site_id=blockchain_data['site_id']).id
        data_collection = {
            'site' : blockchain_data['site_id'],
            'blockchain' : blockchain_id
        }
        siteBlockchain = SiteBlockchainSerializer(data=data_collection)
        if siteBlockchain.is_valid():
            siteBlockchain.save()
            return Response("Done", status=CREATED)
        else:
            return Response(siteBlockchain.errors, status=INVALID_DATA)

    def partial_update(self, request, pk=None):
        blockchain = Blockchian.objects.get(id=pk)
        updated_blockchain = BlockchainSerializer(blockchain, data=request.data, partial=True)
        if updated_blockchain.is_valid():
            updated_blockchain.save()
            return Response("Done", status=SUCCEEDED_REQUEST)
        else:
            return Response(updated_blockchain.errors, status=INVALID_DATA)

    @action(detail=True, methods=['GET'])
    def list(self, request, site_id=None):
        _blockchain = SiteBlockhain.objects.all().filter(site_id=site_id)

        if _blockchain.exists():
            for blockchain in _blockchain.values():
                blockchain_obj = Blockchian.objects.filter(id=blockchain['blockchain_id']).values()[0]

        return Response(blockchain_obj, status=SUCCEEDED_REQUEST)

class LoginView(viewsets.ViewSet):

    def create(self, request):
        login_data = request.data
        site_id = login_data.pop('site_id')

        data = LoginSerializer(data=login_data)
        if data.is_valid():
            data.save()
            login_id = Login.objects.get(url=login_data['url']).id
            data_collection = {
                'site' : site_id,
                'login' : login_id
            }
            siteLogin = SiteLoginSerializer(data=data_collection)
            if siteLogin.is_valid():
                siteLogin.save()
                return Response("Done", status=SUCCEEDED_REQUEST) 
            else:
                return Response(siteLogin.errors, status=INVALID_DATA) 
            
        else:
            return Response(data.errors, status=INVALID_DATA) 
      
    def partial_update(self, request, pk=None):
        login = Login.objects.get(id=pk)
        updated_login = LoginSerializer(login, data=request.data, partial=True)
        if updated_login.is_valid():
            updated_login.save()
            return Response("Done", status=SUCCEEDED_REQUEST)
        else:
            return Response(updated_login.errors, status=INVALID_DATA)

    def destroy(self, request, pk=None):
        login = Login.objects.filter(id=pk)
        if login.exists():
            login.delete()
            return Response("Done", status=SUCCEEDED_REQUEST)
        else:
            return Response("No Item", status=NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def login_admin(self,request):
        data = request.data
        site_object = Site.objects.filter(siteName=data['siteName'], 
                                       adminUsername=data['adminUsername'],
                                       adminPassword=data['adminPassword'])

        if site_object.exists():
            site_id = site_object.values()[0]['id']

            siteLogin_object = SiteLogin.objects.filter(site_id=site_id)
            if siteLogin_object.exists():
                login_id = siteLogin_object.values()[0]['login_id']
            else:
                login_id = None

            siteBlockchain_object = SiteBlockhain.objects.filter(site_id=site_id)
            if siteBlockchain_object.exists():
                blockchain_id = siteBlockchain_object.values()[0]['blockchain_id']    
            else:
                blockchain_id = None     

            data_coll = {
                "exist" : True,
                "site_id" : site_id,
                "login_id": login_id,
                "blockchain_id": blockchain_id
            }
            return Response(data_coll, status=SUCCEEDED_REQUEST)
        else:
            return Response({"exist": False}, status=NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def login_user(self, request):
        data = request.data
        site_object = Site.objects.filter(siteName=data['siteName'])

        if site_object.exists():
            site_id = site_object.values()[0]['id']
            siteLogin_obj = SiteLogin.objects.filter(site=site_id)

            if siteLogin_obj.exists():
                login_id = siteLogin_obj.values()[0]['login_id']
                login_info = Login.objects.filter(id=login_id).values()
                data = login_info[0]
                data['site_id'] = site_id
                return Response(data, status=SUCCEEDED_REQUEST)
            
            else:
                return Response('Login URL have not set yet.', status=NOT_FOUND)

        else:
            return Response('This Company does not exist.', status=NOT_FOUND)

class AllInfoView(viewsets.ViewSet):
    
    def list(self, request, site_id):
        siteLogin_obj = SiteLogin.objects.filter(site_id=site_id)  
        siteBlockchain_obj = SiteBlockhain.objects.filter(site_id=site_id)
        login_obj = None
        blockchain_obj = None

        if siteLogin_obj.exists():
            login_id = siteLogin_obj.values()[0]['login_id']
            login_obj = Login.objects.filter(id=login_id).values()[0]

        if siteBlockchain_obj.exists():
            blockchain_id = siteBlockchain_obj.values()[0]['blockchain_id']
            blockchain_obj = Blockchian.objects.filter(id=blockchain_id).values()[0]

        all_info = {
            "login": login_obj,
            "blockchain": blockchain_obj
        }

        return Response(all_info, status=SUCCEEDED_REQUEST)

class sendEmail(viewsets.ViewSet):

    @action(detail=True, methods=['POST'])
    def success(self, request):
        try:
            print(request.data)
            reciever = request.data['email']
            code = self.get_random_string(6)
            body = '''
                Hello 
                This is an email for verification. Please enter the following code to access the application.
                The verification code is:  
            ''' + code

            yag = yagmail.SMTP('swe.boloori@gmail.com', 'ltfqrmigcunfdhap')
            yag.send(reciever, 'Code Verification', body)
            return Response(code, status=SUCCEEDED_REQUEST)

        except Exception as e:
            return Response("Email Address is wrong", status=INVALID_DATA)
            
        
        

    def get_random_string(self, length):
        
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
