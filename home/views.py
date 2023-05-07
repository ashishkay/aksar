#from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from .models import Donor
from .serializers import DonorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def donor(request, format=None):

    if request.method == 'GET':
        donors = Donor.objects.all()
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def donor_detail(request,id, format=None):

    try:
        donor = Donor.objects.get(pk=id)
    except Donor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DonorSerializer(donor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DonorSerializer(donor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def donation(request):
    mymembers = Donor.objects.all().values()
    template = loader.get_template('all_donation.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Donor.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
