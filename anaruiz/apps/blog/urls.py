from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'<int:year>/<int:month>/<int:day>/<slug:slug>', views.Single.as_view(), name='single'),
    path('member', views.member, name='member'),
    path('send_emails', views.send_emails, name='send_emails'),
]
