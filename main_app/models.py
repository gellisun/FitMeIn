from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

GENDER = (('M', 'Male'),('F', 'Female'),('O', 'Other'))

ACTIVITIES = (('RU','Running'),('WL', 'Weight Lifting'),('GC','Group Classes'),('BR', 'Bike Riding'),('TE','Tennis'),('SQ','Squash'),('WA','Walking'),('BA','Badminton'),('SW','Swimming'),('WA','Walking'),('HI','Hiking'), ('P', 'Pilates'), ('SU', 'Surfing'), ('SK', 'Skateboarding'))

def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField(validators=[MinValueValidator(0)], default=0)  
    location = models.CharField(max_length=50)
    is_couch_potato = models.BooleanField(default=True)
    favorites = models.CharField(max_length=2, choices=ACTIVITIES, default='RU')
    is_active=models.BooleanField(default=False)
    chosen_activities = models.CharField(max_length=2, choices=ACTIVITIES, default='RU')
    latitude = models.FloatField(null=False, blank=True, default=51.515425825794125)
    longitude = models.FloatField(null=False, blank=True, default=-0.07266577316737018)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('profile')
    
class Badges(models.Model):
    name = models.CharField()
    icon = models.ImageField(max_length=255, upload_to=get_profile_image_filepath)
    profile = models.ManyToManyField(Profile)

def get_profile_image_filename(self):
    return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
  
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}" 
    
class Photo(models.Model):
  url = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for user_id: {self.user_id} @{self.url}"