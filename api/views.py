import json
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

from api.models import Estado
from api.serializers import EstadoSerializer


class EstadoDados(APIView):
    def get(self, request, sigla):
        try:
            if sigla =='':
                return JsonResponse({'mensagem':"A sigla do estado nao pode ser vazia"}, status=status.HTTP_400_BAD_REQUEST)
            request = requests.get("http://appcovid19br.herokuapp.com/api/brazil/{0}?limit=1".format(sigla))
            todos = json.loads(request.content)
            for resultado in todos:
                estado = Estado(resultado['state'], resultado['totalCases'], resultado['recovered'], resultado['vaccinated'], resultado['deaths'])
            serializer = EstadoSerializer(estado)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem':"Ocorreu um erro no servidor"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


