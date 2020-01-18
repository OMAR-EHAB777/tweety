from django.contrib import admin
from tweets.models import tweets, comments
# Register your models here.
admin.site.register(tweets)
admin.site.register(comments)