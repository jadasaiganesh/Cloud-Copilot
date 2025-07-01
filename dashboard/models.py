from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} Profile"


from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # like 'amazon-ec2'
    category = models.CharField(max_length=50)
    description = models.TextField()
    details = models.TextField()  # long content for detail page
    icon = models.CharField(max_length=50, default='bi-cloud-fill')  # Bootstrap icon class

    def __str__(self):
        return self.name
