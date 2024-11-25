from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('base/', v.base, name="base"),
    path('contact/', v.contact, name="contact"),
    path('index/', v.index, name="index"),
    path('student/', v.student, name="student"),
    path('sample/', v.sample, name="sample"),
    path('register/', v.register, name="register"),
    path('login/', v.Userlogn, name="login"),
    path('logout/', v.uslogout, name='uslogout'),
    path('items/', v.items, name='items'),
    path('itemlist/', v.itmlist, name='itmlist'),
    path('item/<int:pk>/delete/', v.delt, name='delete'),
    path('item/<int:pk>/edit/', v.editt, name='edit'),

]