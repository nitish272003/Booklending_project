from django.shortcuts import render

# Create your views here.

def get_home(request):
    return render(request,'index.html',{'name1': 'pugal',
                                        'name2': 'user'})
