from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework import viewsets


# using class to do crud operation
class ClassPerson(APIView):
    def get(self, request):
        queryset = Person.objects.filter(team__isnull=False)
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    

# using function to do crud operation

@api_view(["GET","POST"])
def indexView(request):
    if request.method == "GET":
        people_detail = {
            'name'  : 'Adhu',
            'age' : 23,
            'job' : 'Software Deve'
        }
    
        return Response(people_detail)
    
    elif request.method == "POST":
        return Response({
            "Its a POST method"
        })
        
        
@api_view(["GET","POST","PUT","PATCH","DELETE"]) 
def personView(request):
    if request.method == "GET":
        queryset = Person.objects.filter(team__isnull=False)
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PUT":
        data = request.data
        get_query = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(get_query, data=data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        data = request.data
        get_query = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(get_query, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "DELETE":
        data = request.data
        del_query = Person.objects.get(id=data['id'])
        del_query.delete()
        return Response({'This Person data is deleted'})
    
    
# viewSet method to do CRUD operation builtin operation done by django itself
class personViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
    
    def list(self, request):
        search = request.GET.get("search")
        queryset = self.queryset
        
        if search:
            queryset = queryset.filter(name__startswith = search)
            
        if queryset.exists():
            serilizer = PersonSerializer(queryset, many = True)
            return Response({'status' : 200, 'data': serilizer.data})
        else:
            return Response({'status':404, 'data':'No user found'})