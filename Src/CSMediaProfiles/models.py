from django.db import models
from django.contrib.auth.models import User
from .utils import get_slug_url
from django.template.defaultfilters import slugify
from django.db.models import Q

# Create your models here.

# To manage profiles
class CSMediaProfileManager(models.Manager):
    def get_all_csmedia_notfriend_profiles(self, sender):
        csmedia_profiles = CSMediaProfile.objects.all().exclude(csmedia_user=sender)
        csmedia_profile = CSMediaProfile.objects.get(csmedia_user=sender)
        notfriend_queryset = CSMediaRelationship.objects.filter(Q(friend_request_sender=csmedia_profile) | Q(friend_request_receiver=csmedia_profile))
        
        request_accepted = set([])
        for rs in notfriend_queryset:
            if rs.friend_request_status == 'Accepted':
                request_accepted.add(rs.friend_request_receiver)
                request_accepted.add(rs.friend_request_sender)

        request_available = [csmedia_profile for csmedia_profile in csmedia_profiles if csmedia_profile not in request_accepted]

        return request_available

    def get_all_csmedia_profiles(self, me):
        csmedia_profiles = CSMediaProfile.objects.all().exclude(csmedia_user=me) 
        return csmedia_profiles

# Profile Model
class CSMediaProfile(models.Model):
    first_name = models.CharField(max_length=200, blank=True) # blank=True making field optional
    last_name = models.CharField(max_length=200, blank=True)
    csmedia_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(default="Hello CSMedia!", max_length=350)
    email_address = models.EmailField(max_length=200, blank=True)
    user_avatar = models.ImageField(default='csmedia_avatar.png', upload_to='avatars/')
    user_friends = models.ManyToManyField(User, blank=True, related_name='Friends')
    url_slug = models.SlugField(unique=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    objects = CSMediaProfileManager()

    def get_csmedia_friends(self):
         return self.user_friends.all()
        
    def get_csmedia_friends_number(self):
        return self.user_friends.all().count()
    
    def get_csmedia_post_number(self):
         return self.Posts.all().count()
    
    def get_csmedia_posts(self):
         return self.Posts.all()
    
    def get_csmedia_likes_given(self):
        likes_given = self.csmedialike_set.all()
        total_likes_given = 0
        for item in likes_given:
            if item.post_like == 'Like':
                total_likes_given += 1
        return total_likes_given 
        
    def get_csmedia_likes_received(self):
        csmedia_posts = self.Posts.all()
        total_likes_received = 0
        for item in csmedia_posts:
            total_likes_received += item.post_likes.all().count()
        return total_likes_received

    def __str__(self):
        return f"{self.csmedia_user.username}-{self.created_time.strftime('%d-%m-%Y, %H:%M:%S')}"
    
    def save(self, *args, **kwargs):
        slug_exists = False
        if self.first_name and self.last_name:
            to_url_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            slug_exists = CSMediaProfile.objects.filter(url_slug=to_url_slug).exists()
            while slug_exists: 
                to_url_slug = slugify(to_url_slug + " " + str(get_slug_url()))
                slug_exists = CSMediaProfile.objects.filter(url_slug=to_url_slug).exists()
        else:
            to_url_slug = str(self.csmedia_user)
        self.url_slug = to_url_slug
        super().save(*args, **kwargs)

        
FRIEND_REQUEST_STATUS_CHOICES = (
    ('Send', 'Send'),
    ('Accepted', 'Accepted')
)

class CSMediaRelationshipManager(models.Manager):
    def friend_invite_received(self, receiver):
        invite_received_queryset = CSMediaRelationship.objects.filter(friend_request_receiver=receiver, friend_request_status='Send')
        return invite_received_queryset

class CSMediaRelationship(models.Model):
    friend_request_sender = models.ForeignKey(CSMediaProfile, on_delete=models.CASCADE, related_name='sender')
    friend_request_receiver = models.ForeignKey(CSMediaProfile, on_delete=models.CASCADE, related_name='receiver')
    friend_request_status = models.CharField(max_length=10, choices=FRIEND_REQUEST_STATUS_CHOICES)

    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    objects = CSMediaRelationshipManager()

    def __str__(self):
        return f"{self.friend_request_sender}-{self.friend_request_receiver}-{self.friend_request_status}"



