from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120)
    subject= models.CharField(max_length=120,blank=True,null=False)
    message = models.CharField(max_length=200, blank=False, null=False)
    to = models.CharField(max_length=120, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.email