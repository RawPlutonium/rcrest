from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.start,name='index'),
	url(r'^about/$',views.about,name='about'),
	url(r'^post-order/$',views.post_order,name='post-order'),
]