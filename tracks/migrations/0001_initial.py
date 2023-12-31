# Generated by Django 3.2.20 on 2023-08-16 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_ref', models.URLField(blank=True)),
                ('title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('cover_art', models.ImageField(default='../no_image_found_yzsd7j', upload_to='images/')),
                ('genre', models.IntegerField(choices=[(0, 'No genre'), (1, 'Pop'), (2, 'Rock'), (3, 'Hip-Hop'), (4, 'Country'), (5, 'R&B'), (6, 'Folk'), (7, 'Jazz'), (8, 'Metal'), (9, 'EDM'), (10, 'Soul'), (11, 'Funk'), (12, 'Reggae'), (13, 'Punk'), (14, 'Classical'), (15, 'Trap')], default=0)),
                ('opinion', models.TextField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
