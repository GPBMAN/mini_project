
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PromoCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    discount = models.IntegerField(default=10)  # % знижки
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Promocode - {self.user.username}"

    class Meta():
        verbose_name = "PromoCode"
        verbose_name_plural = "PromoCodes"

class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Project - {self.name}"

class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    original_image = models.ImageField(upload_to='media/original/')
    thumbnail = models.ImageField(upload_to='media/thumbs/', blank=True)
    medium_image = models.ImageField(upload_to='media/medium/', blank=True)
    large_image = models.ImageField(upload_to='media/large/', blank=True)
    alt_text = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} Gallery"