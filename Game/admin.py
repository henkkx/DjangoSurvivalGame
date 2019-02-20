from django.contrib import admin
from Game.models import Player, Badge, Achievement

#These classes allow us to add extra functionality to the admin page
class PlayerAdmin(admin.ModelAdmin):
    pass
    
class AchievementAdmin(admin.ModelAdmin):
    pass

class BadgeAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Badge, BadgeAdmin)
