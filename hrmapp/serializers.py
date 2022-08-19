from rest_framework import serializers
from .models import  User
from .models import Leave
from .models import Feedback


class LeaveSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        
        model = Leave
        fields = ['id','user','status','date_from','date_to']
        # fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        
        model=Feedback
        # fields=['id','content','user']
        fields = '__all__'