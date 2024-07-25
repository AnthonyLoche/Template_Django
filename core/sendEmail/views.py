from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import ast

class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        subject = request.data.get("subject")
        message = request.data.get("message")
        recipient_list = request.data.get("recipient_list")
        from_email = request.data.get("from_email")
        
        if isinstance(recipient_list, str):
            recipient_list = ast.literal_eval(recipient_list)
        
        try:
            send_mail(
                subject,
                message,
                from_email=from_email,
                recipient_list=recipient_list,
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except ValidationError as e:
            return HttpResponse(str(e))
        return HttpResponse(
            {"Email enviado com sucesso"}, status=status.HTTP_200_OK
        )
