from rest_framework import serializers
from api.models import Company,Employee

# serializer allow complex data like instances of model to convert into native 
#python data types that can then be easily rendered in json/xml
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # we can make meta class in hyperlinkedModelSerializer class
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields='__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # the is is primary key and primary key is not exposed so to expose it  we use serializer.ReadOnlyField()
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields='__all__'