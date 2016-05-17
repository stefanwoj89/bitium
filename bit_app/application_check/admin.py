from django.contrib import admin
from models import App
from models import AppUser
# Register your models here.
class AppAdmin(admin.ModelAdmin):
	fields = ('name', 'url')

class AppUserAdmin(admin.ModelAdmin):
	fields = ('app', 'user')
	
admin.site.register(App, AppAdmin)
admin.site.register(AppUser, AppUserAdmin)