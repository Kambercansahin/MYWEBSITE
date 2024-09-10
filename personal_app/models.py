from django.db import models


class Home(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    message=models.CharField(max_length=100)
    def __str__(self):
        return f"Name:{self.name}, Email:{self.email},Message:{self.message}"
    
class About(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField(default="")
    email= models.EmailField()
    phone = models.CharField(max_length=15)
    school= models.CharField(max_length=150,default="")
    def __str__(self):
        return f"Name:{self.name} ,\n Bio:{self.bio},\n Email:{self.email},\n Phone:{self.phone}, \n School:{self.school} "
    

class Contact(models.Model):
    email=models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.CharField(max_length=100)
    instagram= models.CharField(max_length=100)
    git_hub=models.CharField(max_length=150, default="")
    def __str__(self):
        return f"Email:{self.email},\n Phone:{self.phone},\n Linkedin:{self.linkedin},\n Instagram:{self.instagram},\n GitHub={self.git_hub}"

class Work(models.Model):
    python = models.CharField(max_length=50)
    java=models.CharField(max_length=50)
    c = models.CharField(max_length=30)
    django = models.CharField(max_length=50)
    Html = models.CharField(max_length=30)
    css = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=100,default="")
    git_hub=models.CharField(max_length=150, default="")
    email=models.EmailField(default="")
    def __str__(self):
        return f"Python:{self.python}, Java:{self.java},C : {self.c},Django:{self.django} Html:{self.Html},Css:{self.css},Linkedin:{self.linkedin},Github:{self.git_hub}"
    

