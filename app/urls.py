
from django.urls import path
from app.views import *

urlpatterns = [
    path('mymodel_json/', mymodel_json, name='mymodel_json'),
    path('mymodel/', mymodel_list, name='mymodel-list'),
]
