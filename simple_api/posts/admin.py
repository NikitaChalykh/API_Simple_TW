from django.contrib import admin

from .models import FavoritePost, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'author',
        'date'
    )
    list_filter = ('author', 'date',)
    empty_value_display = '-пусто-'


class FavoritePostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post'
    )
    list_filter = ('user',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(FavoritePost, FavoritePostAdmin)
