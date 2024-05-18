from django.http import HttpResponse,JsonResponse
def home(request):
   list=["hello","jeena","add","subtract"]
   return JsonResponse(list,safe=False)