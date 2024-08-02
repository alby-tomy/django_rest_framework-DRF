from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view




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
        
        
