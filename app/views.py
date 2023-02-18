from django.shortcuts import render

from .models import user
from .serializers import userserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin



# Create your views here.

class userfirst(GenericAPIView, ListModelMixin, CreateModelMixin):
    '''
    This class lists or displays all the users and also creates a new user in existing model
    '''
    queryset = user.objects.all()                               #Fetches all the objects from user
    serializer_class = userserializer

    def get(self, request, *args, **kwargs):                    #List all the users
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):                   #Create a new User
        return self.create(request, *args, **kwargs)
    
class usersecond(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    '''
    This class is responsible for get, update and delete operation
    '''
    queryset = user.objects.all()
    serializer_class = userserializer

    def get(self, request, *args, **kwargs):                    #Get a User with specific id
        return self.retrieve(request, *args, **kwargs)
    

    def put(self, request, *args, **kwargs):                    #Update a User
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):                 #Delete a User
        return self.destroy(request, *args, **kwargs)