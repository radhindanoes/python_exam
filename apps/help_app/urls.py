from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wishes$', views.index),
    url(r'^log_out$', views.log_out),
    url(r'^add_wish$', views.add_wish),
    url(r'^add$', views.add),
    url(r'^view_job/(?P<num>\d+)$', views.view_job),
    url(r'^delete/(?P<num>\d+)$', views.delete),
    url(r'^edit_wish/(?P<num>\d+)$', views.edit_wish),
    url(r'^update/(?P<num>\d+)$', views.update),
    url(r'^add_to_my_job/(?P<num>\d+)$', views.add_to_my_job),

    url(r'^like_job/(?P<job_id>\d+)$', views.like_job),

    url(r'^view_stats$', views.view_stats),
   
   
   
]