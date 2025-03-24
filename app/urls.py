from django.urls import path,include
from . import views
urlpatterns = [
    
    
    path("",views.SignupPage,name = "signup"),
    path("index/",views.Indexpage,name = "index"),
    path("register/",views.RegisterUser,name = "register"),
    path("otppage/",views.OTPPage,name = "otppage"),
    path("otpverify/",views.Otpverify,name = "otpverify"),
]