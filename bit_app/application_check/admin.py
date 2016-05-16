from django.contrib import admin
from models import App
from models import AppUser
# Register your models here.
class AppAdmin(admin.ModelAdmin):
	pass
class AppUserAdmin(admin.ModelAdmin):
	pass
admin.site.register(App, AppAdmin)
admin.site.register(AppUser, AppUserAdmin)