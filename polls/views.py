from django.template import loader
from .models import MenuItem
from django.http import HttpResponse

def index(request):
	#return HttpResponse("Hello, world. You're at the polls index")
	all_items = MenuItem.objects.all()
	template = loader.get_template('index.html')
	context = {
		'all_items': all_items,
	}
	return HttpResponse(template.render(context, request))