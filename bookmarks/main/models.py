from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    #registration_date = models.DateTimeField('date registered')
    
    #def __str__(self):
    #    return self.author_username
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
    


class Link(models.Model):
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    tags = models.ManyToManyField(Tag)
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.title
    
    
    #def __str__(self):