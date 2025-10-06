from django.db import models
from django.core.validators import FileExtensionValidator
from CSMediaProfiles.models import CSMediaProfile

# Create your models here.

# Post model
class CSMediaPost(models.Model):
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='CSMediaPosts', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    post_likes = models.ManyToManyField(CSMediaProfile, blank=True, related_name='Likes')
    updated_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(CSMediaProfile, on_delete=models.CASCADE, related_name='Posts')

    def __str__(self):
        return str(self.post_content[:20])
    
    def number_of_likes(self):
        return self.post_likes.all().count()
    
    def number_of_comments(self):
        return self.CSMediaComment_set.all().count()

    class Meta:
        ordering = ('-created_time',)

# Comment Model
class CSMediaComment(models.Model):
    csmedia_user = models.ForeignKey(CSMediaProfile, on_delete=models.CASCADE)
    csmedia_post = models.ForeignKey(CSMediaPost, on_delete=models.CASCADE)
    comment_body = models.TextField(max_length=350)
    updated_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    
CSMEDIALIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

# Like Model
class CSMediaLike(models.Model):
    csmedia_user = models.ForeignKey(CSMediaProfile, on_delete=models.CASCADE)
    csmedia_post = models.ForeignKey(CSMediaPost, on_delete=models.CASCADE)
    post_like = models.CharField(choices=CSMEDIALIKE_CHOICES, max_length=8)
    updated_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.csmedia_user}-{self.csmedia_post}-{self.post_like}"