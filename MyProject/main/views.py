from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.db.models import Q
from .my_code import hello
from accounts.utils import Util
h1 = hello()
# Create your views here.
class RoomListCreateView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset=Room.objects.all()
    def get(self,request):
        filter_city=self.request.GET.get('city')
        filter_locality=self.request.GET.get('locality')
        rent_range=self.request.GET.get('rent_range')
        if rent_range=="":
            rent_range=100000
        qs=Room.objects.filter(city__icontains=filter_city,locality__icontains=filter_locality,rent_cost__lte=rent_range).filter(is_booked=False)
        serializer=RoomSerializer(qs,many=True,)
        return Response(serializer.data)
    def post(self,request):
        serializer=RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data) 
        return Response(serializer.errors)

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset=Room.objects.all()
    def get(self,request,pk):
        queryRoom=Room.objects.get(id=pk)
        dans=[]
        for i in queryRoom.preferred_tags:
            dans.append(i)
        interested=Interested_Users.objects.filter(room_id=queryRoom)
        self_interests=MyUser.objects.get(user_id=self.request.user.user_id).interests
        print(self_interests)
        match=[]
        for i in interested:
            others_interest=MyUser.objects.get(user_id=i.user_id.user_id).interests
            print(others_interest)
            ans=h1.calculate_interest([self_interests,others_interest])
            match.append(ans)
        serializer1=RoomSerializer(queryRoom)
        serializer2=InterestedUserSerializer(interested,many=True)
        return Response({"Room":serializer1.data,"Preference_Tags":dans,"Interested_Users":serializer2.data,"Percentage_Matches":match})
        # except:
        #     print("In except")
        #     return Response("Room Not Found")
    
class InterestedUserListView(generics.ListCreateAPIView):
    serializer_class = InterestedUserSerializer
    queryset=Interested_Users.objects.all()
    def post(self,request):
        serializer=InterestedUserCreateSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self,request):
        user_id=self.request.GET.get('user_id')
        qs=Interested_Users.objects.filter(user_id=user_id).values_list("room_id")
        rooms=Room.objects.filter(id__in=qs)
        serializer=RoomSerializer(rooms,many=True)
        return Response(serializer.data)


class ContactUsCreateView(generics.CreateAPIView):
    serializer_class=ContactUsCreateSerializer
    queryset=Contact_Us.objects.all()
    def post(self,request,pk):
        k=Room.objects.get(id=pk)
        receiver_email=Room.objects.get(id=pk).created_by.email
        sender_email=MyUser.objects.get(user_id=self.request.user.user_id).email
        serializer=ContactUsCreateSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save(email_sender=sender_email,email_receiver=receiver_email,room_id=k)
            print(serializer.data)
            data_email = {'email_body': serializer.data['email_body'], 'to_email':receiver_email, 'email_subject':serializer.data['email_subject']}     
            Util.send_email(data_email)  
            return Response(serializer.data)
        return Response(serializer.errors)