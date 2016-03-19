from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Main(View):
    def get(self,request):
        return render(request,'main/main.html')