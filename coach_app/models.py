from django.db import models

# creating text from your models
# https://www.youtube.com/watch?v=zTNA0MtZwso

class coaches(models.Model):
    name = models.CharField(max_length=90)
    location = models.CharField(max_length=255)
    pers_type = models.CharField(max_length=100)

def __unicode__(self):
    return u"{}".format(self.name)



