from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CustomUserSerializer, UserRegistrationSerializer, UserLoginSerializer, DeviceSerializer, FitnessSerializer, ReminderSerializer, DisabilitySerializer, OnBoardingSerializer
from .models import User, Disability, Fitness, Device, Reminder, OnBoardingPreferences
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from . import views


class UserRegistrationAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserInfoAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer
    
    def get_object(self):
        return self.request.user
    
class UserListAPIView(APIView):
    def get(self, request):
        # Your logic to retrieve users
        return Response({"users": []})  # Example response

# Define a function to match the URL
def users_list(request):
    # Call the UserListAPIView here or implement logic
    return UserListAPIView.as_view()(request)


# USER VIEWS
@api_view(['GET'])
@permission_classes([AllowAny])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# DISABILITY VIEWS
@api_view(['GET', 'POST'])
def create_disability_list(request):
    if request.method == 'GET':
        disabilities = Disability.objects.all()
        serializer = DisabilitySerializer(disabilities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DisabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def disability_detail(request, pk):
    try:
        disability = Disability.objects.get(pk=pk)
    except Disability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DisabilitySerializer(disability)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DisabilitySerializer(disability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        disability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FITNESS VIEWS
@api_view(['GET', 'POST'])
def fitness_list_create(request):
    if request.method == 'GET':
        fitness_records = Fitness.objects.all()
        serializer = FitnessSerializer(fitness_records, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FitnessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def fitness_detail(request, pk):
    try:
        fitness_record = Fitness.objects.get(pk=pk)
    except Fitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FitnessSerializer(fitness_record)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FitnessSerializer(fitness_record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        fitness_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# DEVICE VIEWS
@api_view(['GET', 'POST'])
def device_list_create(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def device_detail(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# REMINDER VIEWS
@api_view(['GET', 'POST'])
def reminder_list_create(request):
    if request.method == 'GET':
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reminder_detail(request, pk):
    try:
        reminder = Reminder.objects.get(pk=pk)
    except Reminder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ONBOARDING PREFERENCE VIEWS
@api_view(['GET', 'POST'])
def onboarding_preferences_list_create(request):
    if request.method == 'GET':
        preferences = OnBoardingPreferences.objects.all()
        serializer = OnBoardingSerializer(preferences, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        serializer = OnBoardingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def onboarding_preferences_detail(request, pk):
    try:
        preferences = OnBoardingPreferences.objects.get(pk=pk)
    except OnBoardingPreferences.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OnBoardingSerializer(preferences)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = OnBoardingSerializer(preferences, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        preferences.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
