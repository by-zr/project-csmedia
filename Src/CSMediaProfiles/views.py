from django.shortcuts import render, redirect
from .models import CSMediaProfile, CSMediaRelationship
from .forms import CSMediaProfileForm
# Create your views here.

def csmedia_profile_view(request):
    csmedia_profile = CSMediaProfile.objects.get(csmedia_user=request.user)
    csmedia_profile_form = CSMediaProfileForm(request.POST or None, request.FILES or None, instance=csmedia_profile)
    profile_update_confirm = False

    if request.method == 'POST':
        if csmedia_profile_form.is_valid():
            csmedia_profile_form.save()
            profile_update_confirm = True

    profile_view_context = {
        'csmedia_profile': csmedia_profile,
        'csmedia_profile_form': csmedia_profile_form,
        'profile_update_confirm': profile_update_confirm,
    }

    return render(request, 'CSMediaProfiles/myprofile.html', profile_view_context)

def csmedia_friendrequest_view(request):
    csmedia_user = request.user
    csmedia_profile = CSMediaProfile.objects.get(csmedia_user=request.user)
    invite_queryset = CSMediaRelationship.objects.friend_invite_received(csmedia_profile)
    list_queryset = CSMediaProfile.objects.get_all_csmedia_profiles(csmedia_user)
    csmedia_user_list_is_empty = False
    if len(list_queryset) == 0:
        csmedia_user_list_is_empty = True

    invite_request_context = {
        'invite_queryset': invite_queryset,
        'csmedia_user_list_is_empty': csmedia_user_list_is_empty,
        'csmedia_user': csmedia_user,
        'csmedia_profile': csmedia_profile
    }

    return render(request, 'CSMediaProfiles/pendingrequest.html', invite_request_context)

def csmedia_everyone_view(request):
    csmedia_user = request.user
    list_queryset = CSMediaProfile.objects.get_all_csmedia_profiles(csmedia_user)
    csmedia_user_profile = CSMediaProfile.objects.get(csmedia_user=request.user)
    rs_receiver = CSMediaRelationship.objects.filter(friend_request_sender=csmedia_user_profile)
    rs_sender = CSMediaRelationship.objects.filter(friend_request_receiver=csmedia_user_profile)
    friend_receiver = []
    friend_sender = []
    csmedia_user_list_is_empty = False

    for item in rs_receiver:
        friend_receiver.append(item.friend_request_receiver)

    for item in rs_sender:
        friend_sender.append(item.friend_request_sender)

    if len(list_queryset) == 0:
        csmedia_user_list_is_empty = True
        
    everyone_context = {
        'list_queryset': list_queryset,
        'csmedia_user_profile': csmedia_user_profile,
        'friend_receiver': friend_receiver,
        'friend_sender': friend_sender,
        'csmedia_user_list_is_empty': csmedia_user_list_is_empty,     
    }

    return render(request, 'CSMediaProfiles/everyone.html', everyone_context)

def csmedia_friendinvite_view(request):
    csmedia_user = request.user
    invite_queryset = CSMediaProfile.objects.get_all_csmedia_notfriend_profiles(csmedia_user)

    friend_invite_context = {
        'invite_queryset': invite_queryset
    }

    return render(request, 'CSMediaProfiles/toinvite.html', friend_invite_context)

def send_friend_request(request):
    if request.method=='POST':
        send_request_pk = request.POST.get('profile_pk')
        csmedia_user = request.user
        csmedia_sender = CSMediaProfile.objects.get(csmedia_user=csmedia_user)
        csmedia_receiver = CSMediaProfile.objects.get(send_request_pk=send_request_pk)

        rs = CSMediaRelationship.objects.create(friend_request_csmedia_sender=csmedia_sender, friend_request_csmedia_receiver=csmedia_receiver, friend_request_status='send')

    return render(request, 'CSMediaProfiles/sentrequest.html')
