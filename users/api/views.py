from rest_framework.viewsets import ModelViewSet
from users.api.serializers import userserializer
from users.models import User
from users.api import serializers
from django.contrib.auth.hashers import make_password

class userapiviewset(ModelViewSet):
    serializer_class = userserializer
    queryset = User.objects.all()  

    def create(self, request, *args, **kwargs):#post
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)
    

    #PATCH= para actualizat parcialmente un usuarios
    def partial_update(self,request, *args, **kwargs):
        password=request.data['password']
        if password: #pregunta si password es ==null
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)