from django.contrib import admin
from Game.models import PC, Badge, Achievement

'''
These classes allow us to add extra functionality to the admin page.
-list_display allows specified fields to be displayed on admin interface for that model.
-ordering determines which field ordering of database entries is based on for that model.
-actions can be applied to all selected model entries. By default the only availiable action is
delete selected.
'''
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'most_days_survived', 'games_played', 'most_kills', 'most_people', 'most_exp')
    ordering = ['-most_exp']
    actions = ['reset_games_played']

    def reset_games_played(self, request, queryset):
        queryset.update(games_played=0)
    reset_games_played.short_description = "Reset games played for selected players"

    
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('player', 'badge', 'date_awarded')

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'criteria', 'badge_type', 'icon')
    ordering = ['badge_type', 'criteria']

# Register your models here.
admin.site.register(PC, PlayerAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Badge, BadgeAdmin)
