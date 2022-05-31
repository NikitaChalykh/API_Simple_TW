from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    '''Модель постов'''
    text = models.TextField(
        verbose_name='Текст поста'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор поста'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания поста'
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-date']

    def __str__(self):
        return self.text[:15]


class FavoritePost(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_posts',
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='favorite_posts',
        verbose_name='Избранный пост'
    )

    class Meta:
        verbose_name = "Избранный пост"
        verbose_name_plural = "Избранные посты"
        ordering = ['user']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'post'],
                name='unique_favorite'
            )
        ]

    def __str__(self):
        return self.user.username
