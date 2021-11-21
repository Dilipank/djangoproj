from django.urls import path
from testapp import views
from testapp.views import AllDataView

urlpatterns = [
    path('test', views.homepage_view, name='homepage'),
    path('all_data', views.all_data, name="all_data"),
]