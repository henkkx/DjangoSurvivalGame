from django.contrib import admin
from Game.models import Player, Badge, Achievement

#These classes allow us to add extra functionality to the admin page
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'most_dayes_survived', 'most_kills', 'most_people')
    
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('player', 'badge', 'date_awarded')

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'criteria', 'badge_type', 'icon')

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Badge, BadgeAdmin)
