from django.urls import path
from. import views
from .views import send_welcome_email
app_name = "personal_app"
urlpatterns = [
    path("home/",views.Home, name="home"),
    path("about/",views.about, name="about"),
    path("",views.Home, name="Home admin"),
    path("contact/",views.contact, name="contact"),
    path("SendMessage/",views.SendMessage, name="SendMessage"),
    path("work/",views.work, name="work"),
    path('send-welcome-email/', send_welcome_email, name='send_welcome_email'),
    


   
]
