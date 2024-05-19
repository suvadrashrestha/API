from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action,authentication_classes,permission_classes
from api.models import Company,Employee
from rest_framework.response import Response
from api.serializers import CompanySerializer,EmployeeSerializer
# Create your views here.

#view for company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerializer
    
    @action(detail=True,methods=['get'],authentication_classes=[SessionAuthentication, BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def employees(self,request,pk=None):
       try:
            print(request.user)
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
       except Exception as e:
            print(e)
            return Response({
                "message":"company might not exist"
            })
        
   


#view for employee
class EmployeeViewSet(viewsets.ModelViewSet):
    #either  of one authentication should be fulfilled to access employee
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #this permission must be fulfilled in other to access employee
    permission_classes = [IsAuthenticated]
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer