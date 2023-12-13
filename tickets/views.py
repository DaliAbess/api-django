from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Reservation, Movie
from rest_framework.decorators import api_view
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer
from rest_framework.response import Response
from rest_framework import status ,filters
from rest_framework.views import APIView
from django.http import Http404

#1 n
def no_rest_no_model(request):
    guests=[{
        "id":1,
        "name":"abess",
        "mobile":"123"},
        {
        "id":2,
        "name":"Dali",
        "mobile":"123456"}
    ]
    return JsonResponse(guests,safe=False)
def no_rest_with_model(request):


    data=Guest.objects.all()
    response={'guests':list(data.values('name','mobile'))}
    return JsonResponse(response )
#Get & POST
@api_view (['GET','POST'])
def FBV (request):
    if request.method=='GET':
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer= GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@api_view (['GET','PUT','DELETE'])
#custom function search .. update .. delete 
def FBV_pk (request,pk):  
    
    try:

        guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Get  
    if request.method=='GET':
        
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    elif request.method=='PUT':
        serializer= GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        guest.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
#CBV  get post 
class CBV_list(APIView):
    def get(self,request):
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#CBV  put delete  
class CBV_pk(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guests.DoesNotExist :
            raise Http404
    def get(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    def put(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,pk):
        guest=self.get_object(pk)
        
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def jls_extract_def():
    return 'hall'


@api_view (['GET'])
def search (request):
    hall = request.data['hall']
    movie= request.data['movie']
    movies = Movie.objects.filter(

        hall=hall ,
        movie=movie,
    )
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
@api_view (['POST'])
def new_reservation (request):

    movie=Movie.objects.get(hall=request.GET.get('hall',none),movie=request.GET.get('movie',none))
    guest= Guest()
    guest.name=request.GET.get('name',none)
    guest.mobile=request.GET.get('mobile',none)
    guest.save()
    reservation =Reservation()
    reservation.guest=guest
    reservation.movie=movie 
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)

