from typing import Any
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, FormView
from .models import Topico, Tag
from .forms import PostForm, TopicoForm
from django.contrib import messages
# Create your views here.


class Index(ListView):
    model = Topico
    template_name = "index.html"
    context_object_name = "topicos"
    paginate_by = 5

    def get_queryset(self):
        return Topico.objects.all().order_by('-id')


class IndexTag(ListView):
    model = Topico
    template_name = "index.html"
    context_object_name = "topicos"
    paginate_by = 5

    def get_queryset(self):

        tags = self.kwargs.get("tag")
        if tags == 'pesquisa':
            tags = self.request.GET.get('tag')
            print(tags)
            tag = [x for x in tags.split() if x.strip()]

        return Topico.objects.filter(tag__name__in=tag).order_by('-id').distinct()


class TopicoView(DetailView, FormView):
    model = Topico
    template_name = "topico.html"
    context_object_name = "topico"
    slug_url_kwarg = "slug"
    form_class = PostForm

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.visualizacao += 1
        self.object.save()

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):

        self.object = self.get_object()
        form.instance.user = self.request.user
        form.instance.topico = self.object
        form.save()
        self.success_url = self.request.path
        return super().form_valid(form)

    def form_invalid(self, form):
        self.object = self.get_object()
        self.object.visualizacao -= 1
        self.object.save()
        return redirect(self.request.path)


class NewTopico(View):

    def post(self, request):
        form = TopicoForm(request.POST)
        tags_form = request.POST.get('tags')
        tags = [Tag.objects.get_or_create(name=x)
                for x in tags_form.split() if x.strip()]

        if form.is_valid():
            topico = form.save(commit=False)
            topico.user = request.user
            try:
                topico.save()
                for tag in tags:
                    topico.tag.add(tag[0])
                topico.save()
                return redirect('index')
            except Exception as e:
                messages.error(request, 'Tópico não criado')
                return redirect('index')

        else:
            messages.error(request, 'Tópico não criado')
            return redirect('index')
