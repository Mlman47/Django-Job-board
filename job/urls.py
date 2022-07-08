
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.Job_list),
    path('<int:id>', views.Job_detail)
]
