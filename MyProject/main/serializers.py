from rest_framework import serializers
from .models import *
from accounts.serializers import MyUserSerializer

from rest_framework.fields import CurrentUserDefault
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields="__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"

class InterestedUserSerializer(serializers.ModelSerializer):
    user_id=MyUserSerializer()
    tagz=serializers.SerializerMethodField('get_interests')
    def get_interests(self,obj):
        p=[]
        k=MyUser.objects.get(user_id=obj.user_id.user_id).interests
        for i in k:
            p.append(i)
        return p
    class Meta:
        model=Interested_Users
        fields="__all__"

class InterestedUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interested_Users
        fields="__all__"


class ContactUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact_Us
        fields="__all__"