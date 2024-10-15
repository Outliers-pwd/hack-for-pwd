from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


def home(request):
    return Response()