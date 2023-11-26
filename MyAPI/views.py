from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from . models import approvals
from . serializers import approvalsSerializers



import joblib



class ApprovalsView(viewsets.ModelViewSet):
	queryset = approvals.objects.all()
	serializer_class = approvalsSerializers
		
@api_view(["POST"])
def approvereject(request):
	try:

		data = JSONParser().parse(request.data)
		
		model = joblib.load('svm_model.joblib') 
		feature1 = data.budget
		feature2 = data.findingSource
		feature3 = data.TRLSart
		feature4 = data.TRLend
		features = [feature1, feature2 , feature3, feature4]
		predictions = model.predict([features])
		return JsonResponse(predictions)

	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
