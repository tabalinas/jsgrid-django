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
            .filter(name__contains = request.GET.get('name')) \
            .filter(address__contains = request.GET.get('address'));
        return HttpResponse(self.to_json(clients), content_type = 'application/json', status = 200)

    def post(self, request):
        Client.objects.create(
            name = request.POST.get("name"),
            age = request.POST.get("age"),
            address = request.POST.get("address"),
            married =  True if request.POST.get("married") == 'true' else False
        )
        return HttpResponse(status = 201)

    def put(self, request, client_id):
        client = Client.objects.get(pk = client_id)
        client.name = request.PUT.get("name")
        client.age = request.PUT.get("age")
        client.address = request.PUT.get("address")
        client.married = True if request.PUT.get("married") == 'true' else False
        client.save()
        return HttpResponse(status = 200)

    def delete(self, request, client_id):
        client = Client.objects.get(pk = client_id)
        client.delete()
        return HttpResponse(status = 200)

    def to_json(self, objects):
        return serializers.serialize('json', objects)
