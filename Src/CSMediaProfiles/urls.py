from django.urls import path
from .views import csmedia_profile_view, csmedia_friendrequest_view, csmedia_everyone_view, csmedia_friendinvite_view, send_friend_request

app_name = "CSMediaProfiles"

urlpatterns = [
    path('myprofile/', csmedia_profile_view, name='Profile-Page'),
    path('pendingrequest/', csmedia_friendrequest_view, name='Pending-Request-Page'),
    path('everyone/', csmedia_everyone_view, name='All-Profile-Page'),
    path('toinvite/', csmedia_friendinvite_view, name='Available-Invite-Page'),
    path('sentrequest/', send_friend_request, name='Sent-Request-Page'),
 
]

