
from rest_framework import generics, mixins
from ..models import *
from dateutil.parser import parse
from .serializers import *
# from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
# from rest_framework.permissions import AllowAny, IsAuthenticated
import csv
import smtplib
from datetime import datetime, timedelta
from django.utils import timezone
import json
# from rest_framework.pagination import PageNumberPagination
# from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

import requests
import datetime
from email.mime.text import MIMEText
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView



class CreateUserView(generics.CreateAPIView):
	model = get_user_model()
	# permission_classes = (AllowAny,)
	serializer_class = UserSerializer


class UserLoginAPIView(APIView):
	# permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer


	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			usere = serializer.validated_data['email']
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class authdataCreatelView(generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = authSerializer
	# permission_classes = [AllowAny]


	def get_queryset(self):
		return authdataModel.objects.all()

class authdataModelView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = authSerializer
	# permission_classes = [AllowAny]


	def get_queryset(self):
		return authdataModel.objects.all()



class nameslView( generics.CreateAPIView, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = NamesSerializer
	# permission_classes = [AllowAny]


	def get_queryset(self):
		return NamesModel.objects.all()

	def put(self, request, pk, format=None):
		snippet = NamesModel.objects.get(pk=pk)
		serializer = NamesSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response('moma', status=HTTP_200_OK)
		
	def delete(self, request, pk, format=None):
		snippet = NamesModel.objects.get(pk=pk)
		snippet.delete()
		return Response('moma', status=HTTP_200_OK)

	
		