from django.shortcuts import render

# Create your views here.
from django.views.generic.base	import TemplateView
# Create your views here.

class Homepageview(TemplateView):
	template_name='index.html'


class BeverageView(TemplateView):
	template_name='beverages.html'

def item(request, menu_id):
	#template=loader.get_template('menu.html')	
	queryset= Menu_model.objects.filter(category_types=menu_id)
	#print queryset
	context={
	'items':queryset
	}
	#return render(template,render(context,request))
	return render(request,"menu.html",context)