from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from.import models
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from .models import Home

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def Home(request):
    home = models.Home.objects.all()
    home_dic = {"home": home}
    return render (request,"personal_app/APPhome.html",context=home_dic)



def about(request):
    about = models.About.objects.all()
    about_dic = {"about": about}
    return render (request,"personal_app/about.html",context=about_dic)

def contact(request):
    contact=models.Contact.objects.all()
    contact_dic= {"contact": contact}
    return render(request,"personal_app/contact.html",context=contact_dic)



def SendMessage(request):
    if request.POST:
        name=request.POST["name"]
        email=request.POST["email"] 
        message=request.POST["message"]
        models.Home.objects.create(name=request.POST.get('name'), email=request.POST.get('email'), message=request.POST.get('message'))
        return redirect(reverse("personal_app:home"))
    else:
        return render(request,"personal_app/SendMessage.html")



def work(request):
    works=models.Work.objects.all()
    work_dic={"work":works}
    return render(request,"personal_app/work.html",context=work_dic)








@require_http_methods(["GET", "POST"])
def send_welcome_email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        try:
            # E-posta adresini doğrulama
            validate_email(email)
        except ValidationError:
            # Eğer e-posta adresi geçerli değilse, kullanıcıya hata mesajı gösterme
            return render(request, "personal_app/send_email.html", {"error_message": "Geçersiz e-posta adresi."})
        
        # Form verileriyle birlikte e-posta gönderme işlemi
        send_mail(
            subject='New Message from Your Website',
            message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
            from_email=email,  # Gönderenin e-posta adresi
            recipient_list=['cank56150@gmail.com'],  # E-postanın gönderileceği adres
            fail_silently=False,  # Hata oluştuğunda sessizce başarısız olmayı dene
        )
        
        # Veritabanına mesajı kaydetme
        models.Home.objects.create(name=name, email=email, message=message)
        
        # Başarılı bir şekilde mesaj gönderildikten sonra ana sayfaya yönlendirme
        return redirect(reverse("personal_app:home"))
    else:
        # GET isteği alındığında, mesaj gönderme formunu gösterme
        return render(request, "personal_app/send_email.html")
