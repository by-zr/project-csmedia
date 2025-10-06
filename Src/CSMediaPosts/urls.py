from django.urls import path
from .views import csmedia_post_view, csmedia_like_unlike

app_name = 'CSMediaPosts'

urlpatterns = [
    path('', csmedia_post_view, name='Main-Post-Page'),
    path('liked/', csmedia_like_unlike, name='Like-Post-Page')

]