from rest_framework import serializers
from .models import Person, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name']

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    extra_field = serializers.SerializerMethodField()
    
    def get_extra_field(self, obj):
        return "extra field inside serializer"
    
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1
        
    def validate(self,data):
        special_char = "!@#$%^&*_+\-*;~"
        
        if any(c in special_char for c in data['name']):
            raise serializers.ValidationError("Name should not contain any special characters")
            
        if not any(c in special_char for c in data['password']):
            raise serializers.ValidationError(f"Password should contain at least one special character from [ {special_char} ]")
            
        if data['age'] < 18:
            raise serializers.ValidationError("you are under 18")
            
        return data