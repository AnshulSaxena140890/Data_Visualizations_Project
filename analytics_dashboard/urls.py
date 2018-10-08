from django.conf.urls import url
from analytics_dashboard import views

urlpatterns = [
       url(r'^$',views.display),
      

]