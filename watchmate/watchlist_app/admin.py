from django.contrib import admin
from watchlist_app.models import WatchList,StreamingPlatform

# Register your models here.

admin.site.register(WatchList)
admin.site.register(StreamingPlatform)