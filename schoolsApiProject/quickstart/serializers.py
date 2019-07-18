from django.contrib.auth.models import User, Group
from quickstart.models import Schools
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = ('id', 'school_id', 'province_id', 'average')

