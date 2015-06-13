from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

from simple_rest import Resource

from .models import Client

def index(request):
    return render(request, 'index.html')


class Clients(Resource):

    def get(self, request):
        clients = Client.objects.all() \
            .filter(name__contains=request.GET.get('name')) \
            .filter(address__contains=request.GET.get('address'));

        json_serializer = serializers.get_serializer('json')()
        clientsJSON = json_serializer.serialize(clients)

        return HttpResponse(clientsJSON, content_type='application/json', status=200)

