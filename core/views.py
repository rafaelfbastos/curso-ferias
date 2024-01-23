from django.shortcuts import render
from django.views import View
from .models import Topico
# Create your views here.


class Index(View):

    def get(self, request, *args, **kwargs):
        topicos = Topico.objects.all()

        context = {"topicos": topicos}

        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        ...
