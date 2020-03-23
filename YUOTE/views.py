from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from .models import MCompany
# Create your views here.
from .my_serializer.my_serializer import CompanySerializer

class company_list_view(APIView):
    def get(self,reqiest):
        company_list = MCompany.objects.all()
        com_ser =  CompanySerializer(company_list,many=True)
        print(company_list)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': com_ser.data
        })