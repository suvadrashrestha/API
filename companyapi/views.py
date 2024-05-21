from django.http import HttpResponse,JsonResponse

#function based view
# from rest_framework.response import Response



def home(request):
   if(request.method=="GET"):
      return HttpResponse("done")
