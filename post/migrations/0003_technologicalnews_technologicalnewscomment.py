# Generated by Django 3.2.16 on 2022-10-27 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_internationalnewscomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologicalNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='title')),
                ('picture', models.ImageField(null=True, upload_to=post.models.user_directory_path, verbose_name='Picture')),
                ('caption', models.CharField(max_length=500000, verbose_name='Caption')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tag', models.ManyToManyField(related_name='technologicalNews', to='post.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologicalNewsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.technologicalnews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
