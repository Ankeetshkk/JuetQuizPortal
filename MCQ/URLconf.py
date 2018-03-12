from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^\signup',views.signup,name='signup'),
     url(r'^register/$', views.register, name='register'),
    url(r'^password-change-done/$',
        auth_views.password_change_done,
        {'template_name': 'cadmin/password_change_done.html'},
        name='password_change_done'
        )
    
       
        
        ]
