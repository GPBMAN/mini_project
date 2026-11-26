from django.contrib import admin
from . import models as m

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'weight')
    list_filter = ('price', 'category', 'weight')

admin.site.register(m.Category)
admin.site.register(m.Product, ProductAdmin)
admin.site.register(m.UserProfile)

