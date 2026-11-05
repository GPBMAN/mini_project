from django.contrib import admin
from .models import Project, ProjectGallery, PromoCode
# Register your models here.

admin.site.register(PromoCode)
admin.site.register(Project)
admin.site.register(ProjectGallery)