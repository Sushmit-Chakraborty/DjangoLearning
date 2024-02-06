from django.views.generic.base import TemplateView
from django.shortcuts import  render
from .models import Posts

def index(request):
    print("The request method is - "+request.method)
    if request.method == 'POST':
        try:
            data = request.POST['result']
            
            print("The data is - "+str(data))
        except KeyError:
            print("Error")
    
    return render(request,'index.html')
