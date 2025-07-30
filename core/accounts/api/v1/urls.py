from django.urls import path , include
from . import views

app_name = 'api-v1'
urlpatterns = [
    path("registration",views.RegistrationApiView.as_view(),name='registration')
    #path("login/",LoginView.as_view(), name="login"),
    #path("register/", RegisterView.as_view(), name="register"),
]