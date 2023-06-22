from django.http import JsonResponse, HttpResponse
from lliga.models import *

def get_lligues(request):
	lligues = Lliga.objects.all().values()
	return JsonResponse( list(lligues), safe=False )

def get_equips(request,lliga_id):
	lliga = Lliga.objects.get(pk=lliga_id)
	print(lliga)
	#equips = lliga.equips.all().values()
	equips = Equip.objects.filter(lliga=lliga).values()
	if equips:
		return JsonResponse( list(equips), safe=False )
	else: 
		return HttpResponse("No hi ha equips en aquesta lliga!")
