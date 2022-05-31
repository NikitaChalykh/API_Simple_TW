# Generated by Django 2.2.16 on 2022-05-31 16:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст поста')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='FavoritePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_posts', to='posts.Post', verbose_name='Избранный пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_posts', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранный пост',
                'verbose_name_plural': 'Избранные посты',
                'ordering': ['user'],
            },
        ),
        migrations.AddConstraint(
            model_name='favoritepost',
            constraint=models.UniqueConstraint(fields=('user', 'post'), name='unique_favorite'),
        ),
    ]
