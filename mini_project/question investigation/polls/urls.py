from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]

"""
path(route, view, kwargs, name)

kwargs : 뷰에 전달할 값
"""