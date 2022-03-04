from django.contrib import admin
from ads.models import User, Ads, Location, Category


admin.site.register(User)
admin.site.register(Ads)
admin.site.register(Location)
admin.site.register(Category)