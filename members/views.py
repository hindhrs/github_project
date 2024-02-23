from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Autho

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context, request))


def authors(request):
  myautho = Autho.objects.all().values()
  template = loader.get_template('login.html')
  context = {
    'myautho' : myautho,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render(request))