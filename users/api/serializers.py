from rest_framework import serializers
from users.models import User 



class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id','username','first_name','last_name','email','password','is_active','date_joined'
        ]