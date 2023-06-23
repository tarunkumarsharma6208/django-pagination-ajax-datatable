
from django.urls import path
from app.views import *

urlpatterns = [
    # path('latestnews/', display_latestnews, name="display_pagination"),
    # path('mymodel/', MyModelListView.as_view(), name='mymodel-list'),
    
    path('mymodel_json/', mymodel_json, name='mymodel_json'),
    path('mymodel/', mymodel_list, name='mymodel-list'),
]
