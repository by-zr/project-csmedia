from django.http import HttpResponse
from django.shortcuts import render

def csmedia_home_view(request):
    csmedia_user = request.user # dynamic


    home_view_context = {
        'csmedia_user': csmedia_user,
    }

    return render(request, 'main/home.html', home_view_context)