from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        
    def validate(self,data):
        special_char = "!@#$%^&*_+\-*;~"
        
        if any(c in special_char for c in data['name']):
            raise serializers.ValidationError("Name should not contain any special characters")
            
        if not any(c in special_char for c in data['password']):
            raise serializers.ValidationError(f"Password should contain at least one special character from [ {special_char} ]")
            
        if data['age'] < 18:
            raise serializers.ValidationError("you are under 18")
            
        return data