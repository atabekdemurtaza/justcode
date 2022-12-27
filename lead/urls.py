from django.urls import path
from .views import index
from .views import by_rubric
from .views import BbCreateView

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='create'),
    path('', index, name='index'),
]