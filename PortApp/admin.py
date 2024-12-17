from django.contrib import admin
from . models import Profile, Skill, Contactmessage

# Register your models here.

admin.site.register(Profile)

admin.site.register(Skill)

@admin.register(Contactmessage)
class ContactmessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    search_fields = ('name', 'email', 'message')