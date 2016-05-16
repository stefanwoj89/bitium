from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from . models import App, AppUser
import json

def index(request):
	app_list = []
	used_apps_list = []

	if request.method == 'GET':
		apps = App.objects.all()
		for app in apps:
			app_list.append({'name': app.name, 'urls': [app.url]})
	elif request.method == 'POST':
		app_names = request.POST['names'].split(",")
		for app_name in app_names:
			app = App.objects.get(name=app_name)
			au = AppUser.objects.get_or_create(app=app, user=request.user)
	try:
		used_apps = AppUser.objects.filter(user=request.user)
		for au in used_apps:
			used_apps_list.append({'name': au.app.name})
	except AppUser.DoesNotExist:
		used_apps = None

	return render(request, 'application_check.html', {'apps': json.dumps(app_list), 'used_apps': json.dumps(used_apps_list)})