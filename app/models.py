from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topin_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    url=models.URLField()
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self):
        return self.author
    
class capital(models.Model):
    cap_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.cap_name

class country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)
    cap_name=models.ForeignKey(capital,on_delete=models.CASCADE,unique=True)
    def __str__(self):
        return self.country_name


