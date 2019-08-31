from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	context = {}
	template = 'app/table.html'
	return render(request, template, context)


@login_required
def table(request):
	context = {}
	template = 'app/table.html'
	return render(request, template, context)


@login_required
def start(request):
	context = {}
	template = 'app/stats.html'
	return render(request, template, context)