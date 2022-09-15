from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers
from . import models
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




@api_view(['GET'])
def homePage(request):
    return Response({'success': True, 'message': 'Welcome to homepage'}, status=status.HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer


class CompanyViewSet(ModelViewSet):
    queryset = models.Company.objects.all().order_by('-inception_data')
    serializer_class = serializers.CompanySerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated,IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=company_name']
    ordering_fields = ['inception_data']


class TeamViewSet(ModelViewSet):
    queryset = models.Team.objects.all().order_by('-created_at')
    serializer_class = serializers.TeamSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company']

    @action(detail=False, methods=['GET'])
    def allteams(self, request):
        d = {}
        company = models.Company.objects.all()
        for i in company:
            team = models.Team.objects.filter(company__id=i.id)
            serialized_data = serializers.TeamSerializerAll(team, many=True).data
            company_id = str(i.id)
            if company_id not in d:
                d[company_id] = [serialized_data]
            else:
                d[company_id].append(serialized_data)
        return Response(d)


@api_view(['POST'])
def register(request):
    request_map = ['name', 'email', 'phone', 'is_superadmin', 'password']
    data = request.data

    for i in request_map:
        if i not in data:
            return Response(f"{i} is required", status=status.HTTP_400_BAD_REQUEST)

    email = data['email']
    phone_number = data['phone']
    is_super_admin = data['is_superadmin']
    name = data['name']
    password = data['password']

    if models.Account.objects.filter(email=email).exists():
        return Response("Email id already exists", status=status.HTTP_400_BAD_REQUEST)
    if models.Account.objects.filter(phone_number=phone_number).exists():
        return Response("Phone number already exists", status=status.HTTP_400_BAD_REQUEST)

    if is_super_admin:
        acc = models.Account.objects.create_superuser(name, email, email, password)
    else:
        acc = models.Account.objects.create_user(name, email, email, password)

    acc.phone_number = phone_number
    acc.save()
    serializer = serializers.UserSerializerWithToken(acc)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
