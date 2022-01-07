from django.contrib import admin
from .models import ContactForm, Post
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'ALPHA WOMEN INITIATIVE ADMIN PANEL'
admin.site.register(Post)
admin.site.register(ContactForm)


admin.site.unregister(Group)



class AlphaWomwnAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
