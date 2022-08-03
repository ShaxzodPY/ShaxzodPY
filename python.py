from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.db.models import Q

def testing(request):
  mydata = Members.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))