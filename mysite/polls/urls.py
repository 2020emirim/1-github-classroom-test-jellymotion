from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    # 127.0.0.1:8000/polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # 127.0.0.1:8000/polls/5/results/
    path('<int:pk>/results/', views.ResultsView_as_view(), name='results'),
    # 127.0.0.1:8000/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]