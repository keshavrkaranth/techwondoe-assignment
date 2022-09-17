from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'email', 'name')


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'name', 'token', 'is_admin')

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        # In most of the senario we dont send ID for frontend this may cause some serious security breachs insted of this we can use slug
        fields = ('id', 'company_name', 'company_ceo', 'company_address', 'inception_date')


class TeamSerializerAll(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('team_lead', 'created_at')


class TeamSerializer(TeamSerializerAll):
    class Meta:
        model = Team
        fields = ('company', 'team_lead', 'created_at')
