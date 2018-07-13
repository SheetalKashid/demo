from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import employee
import datetime
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
# Create your views here.
def hello(request):
	return HttpResponse("<h2>Hello welcome to my first django page</h2>")

def index(request):

	Employees=employee.objects.all()[:10]
	template=loader.get_template("employee/index.html")
	context={
		'title':'Employee records',
		'employee':Employees
		}
	print(Employees.count())
	#return HttpResponse(request,'employee/index.html',context,content_type="application/xhtml+xml")
	return HttpResponse(template.render(context))
def demo(request):
	now=datetime.datetime.now()
	html="<html><body><h2>The current time is: %s</h2></body></html>"%now
	return HttpResponse(html)

def index3(request):
	template=loader.get_template("employee/demo.html")
	name={
		student:'abc'
	     }
	return HttpResponse(template.render(name))

def index2(request):
	a=1
	if a:
		return HttpResponseNotFound("Page not Found!")
	else:
		return HttpResponse("Page Found!!")

def show(request):
	return HttpResponse("<h1>This is a HTTP GET request</h1>")	


