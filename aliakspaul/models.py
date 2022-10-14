from email.policy import default
from django.db import models


#HOME PAGE
class Home(models.Model):
    name = models.CharField(max_length=30)
    greeting_1 = models.CharField(max_length=10)
    greeting_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='picture/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#ABOUT PAGE
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    email = models.EmailField(max_length=70, blank=True, unique=True, default='-')
    phone = models.CharField(max_length=200, default='-')
    adress = models.CharField(max_length=200, default='-')
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


#SKILLS PAGE
class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self) :
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)


#Portfolio page
class Portfolio(models.Model):
    name = models.CharField(max_length=20, default="Portfolio")
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
 
    def __str__(self) :
        return f'Portfolio{self.id}'
