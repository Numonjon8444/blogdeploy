from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, RasmPageView, VideoPageView
urlpatterns=[
    path('',HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),
    path('contact/',ContactPageView.as_view(), name='contact'),
    path('rasm/', RasmPageView.as_view(), name='rasm'),
    path('vide/', VideoPageView.as_view(), name='vide')
]