from django.urls import path
from .views import Index, TopicoView, IndexTag, NewTopico

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('topico/<slug:slug>', TopicoView.as_view(), name="topico"),
    path('<str:tag>', IndexTag.as_view(), name="index-tag"),
    path('new-topico/', NewTopico.as_view(), name='new-topico'),
    path('pesquisa', IndexTag.as_view(), name="pesquisa"),

]
