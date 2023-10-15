from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .data import data
import requests
from django.core.mail import send_mail
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse
from server.settings import BASE_DIR, MEDIA_ROOT

# Create your views here.

class Education(APIView):
    def get(self, request):
        return Response(data["my_education"], content_type = 'application/json')

class Experience(APIView):
    def get(self, request):
        return Response(data["experiences"], content_type = 'application/json')

class Certification(APIView):
    def get(self, request):
        return Response(data["certifications"], content_type = 'application/json')

class Project(APIView):
    def get(self, request):
        return Response(data["projects"], content_type = 'application/json')

class Skills(APIView):
    def get(self, request):
        return Response(data["skills"], content_type = 'application/json')

class ContactData(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        subject = request.data['subject']
        message = request.data['message']
    
        if name == "" or email == "" or subject == "" or message == "":
            return Response({'msg':'Please fill all details !',
            'type': 'error'
            }, content_type = 'application/json')
        elif '@' in email:
            lst = email.split('@')
            i = '@' + lst[-1]
            if i in ['@gmail.com','@outlook.com','@hotmail.com','@yahoo.com']:
                contact_data = {
                    'name' : name,
                    'email' : email,
                    'subject' : subject,
                    'message' : message
                }
                requests.post('https://myportfolio-378d6-default-rtdb.firebaseio.com/data.json',
                json = contact_data)

                msg = f"Name : {name} \nEmail : {email} \nMessage : {message}"
                send_mail(
                subject = subject,
                message = msg,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list=['vipul.mash1710@gmail.com'])
            
                return Response({'msg':'Message Send Successfully',
                'type' : 'success'}, content_type = 'application/json')
            else:
                return Response({'msg':'Please Check Details!',
                'type' : 'warning'}, content_type = 'application/json')
        else:
            return Response({'msg':'Please Check Details!',
            'type' : 'warning'}, content_type = 'application/json')

class Download(APIView):
    def get(self,request):
        path_to_file = MEDIA_ROOT + '/resume.pdf'
        f = open(path_to_file, 'rb')
        pdfFile = File(f)
        response = HttpResponse(pdfFile.read())
        response['Content-Disposition'] = 'attachment'
        return response