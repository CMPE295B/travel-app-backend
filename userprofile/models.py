from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    phone = models.IntegerField()
    company_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=30)
    website = models.URLField(blank=True)
    
User.profile = property(lambda u:UserProfile.obects.get_or_create(user=u)[0])