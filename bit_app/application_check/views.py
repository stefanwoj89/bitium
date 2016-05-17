from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from . models import App, AppUser
import json

def index(request):
	app_list = []
	used_apps_list = []
	unused_apps_list = []
	if request.method == 'GET':

		apps = App.objects.all()
		for app in apps:
			app_list.append({'name': app.name, 'urls': [app.url]})
		return render(request, 'application_check.html', {'apps': json.dumps(app_list)})

	elif request.method == 'POST':
		
		app_names = request.POST['names'].split(",")		
		unused_apps = App.objects.exclude(name__in=app_names)
		for unused_app in unused_apps:
			unused_apps_list.append({'name': unused_app.name})

		for app_name in app_names:
			if app_name == '':
				continue
			app = App.objects.get(name=app_name)
			au = AppUser.objects.get_or_create(app=app, user=request.user)

		used_apps = AppUser.objects.filter(user=request.user)
		for au in used_apps:
			used_apps_list.append({'name': au.app.name})
			
		post_response_data = {}
		post_response_data['used_apps_list'] = used_apps_list;
		post_response_data['unused_apps_list'] = unused_apps_list;

		return HttpResponse(json.dumps(post_response_data), content_type="application/json")