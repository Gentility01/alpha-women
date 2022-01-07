from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to = 'pictures/', blank = True, null = True, validators = [FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    title = models.CharField(max_length=100)
    cotent = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    Administrators = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})





class ContactForm(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    message = models.TextField(default="enter your message here")
    male = models.BooleanField("MALE", default=False)
    female = models.BooleanField("FEMALE", default=False)
    
    # date_posted = models.DateField(default=timezone.now)
    




    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height >300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    # class Meta:
    #     ordering = ('-created',)


    # img = Image.open(self.picture.path)

    # if img.height > 300 or img.width > 300:
    #     output_size = (300,300) 
    #     img.thumbnail(output_size)
    #     img.save(self.picture.path)


