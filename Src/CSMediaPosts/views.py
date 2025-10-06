from django.shortcuts import render, redirect
from .models import CSMediaPost, CSMediaLike
from CSMediaProfiles.models import CSMediaProfile
from .forms import CSMediaPostForm, CSMediaCommentForm

# Create your views here.

def csmedia_post_view(request):
    csmedia_queryset = CSMediaPost.objects.all()
    csmedia_profile = CSMediaProfile.objects.get(csmedia_user=request.user)

    # initialise post & comment form
    csmedia_post_form = CSMediaPostForm()
    csmedia_comment_form = CSMediaCommentForm()
    csmedia_add_post = False
    csm_profile = CSMediaProfile.objects.get(csmedia_user=request.user)

    if 'submit_post_form' in request.POST:
        print(request.POST)

        csmedia_post_form = CSMediaPostForm(request.POST, request.FILES)
        if csmedia_post_form.is_valid():
            instance = csmedia_post_form.save(commit=False)
            instance.post_author = csm_profile 
            instance.save()
            csmedia_post_form = CSMediaPostForm()
            csmedia_add_post = True

    if 'submit_comment_form' in request.POST:
        csmedia_comment_form = CSMediaCommentForm(request.POST)
        if csmedia_comment_form.is_valid():
            instance = csmedia_comment_form.save(commit=False)
            instance.csmedia_user = csm_profile
            instance.csmedia_post = CSMediaPost.objects.get(id=request.POST.get('post_id'))
            instance.save()
            csmedia_comment_form = CSMediaCommentForm()
            csmediapost = CSMediaPost.objects.get(id=request.POST.get('post_id'))

    post_view_context = {
        'csmedia_queryset': csmedia_queryset,
        'csmedia_profile': csmedia_profile,
        'csmedia_post_form': csmedia_post_form,
        'csmedia_comment_form': csmedia_comment_form,
        'csmedia_add_post': csmedia_add_post,

    }

    return render(request, 'CSMediaPosts/main.html', post_view_context)

def csmedia_like_unlike(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_object = CSMediaPost.objects.get(id=post_id)
        profile = CSMediaProfile.objects.get(csmedia_user=user)

        if profile in post_object.post_likes.all():
            post_object.post_likes.remove(profile)
        else:
            post_object.post_likes.add(profile)

        like, created = CSMediaLike.objects.get_or_create(csmedia_user=profile, csmedia_post_id=post_id)

        if not created:
            if like.post_like=='Like':
                like.post_like=='Unlike'
            else:
                like.post_like=='Like'
        else:
            like.post_like=='Like'
        
            post_object.save()
            like.save()

    return redirect('CSMediaPosts:Main-Post-Page')

    