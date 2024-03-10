from django.contrib.auth.models import User
from django.db import models


class hoteldetails(models.Model):
    hotelname = models.CharField(max_length=255)
    noofrooms = models.IntegerField()
    hoteldesc = models.TextField()
    hotellocation = models.CharField(max_length=255)
    hotelavgroomcostpn = models.IntegerField()
    hotelimage = models.ImageField(upload_to='static/media/hotelimages/', null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/media/profile_pics/', blank=True)
