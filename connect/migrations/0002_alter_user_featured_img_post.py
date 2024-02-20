# Generated by Django 5.0.2 on 2024-02-20 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='featured_img',
            field=models.ImageField(null=True, upload_to='profile_imgs/'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=400, null=True)),
                ('add_photos', models.ImageField(null=True, upload_to='post_imgs/')),
                ('add_location', models.CharField(max_length=50, null=True)),
                ('add_tags', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connect.user')),
            ],
        ),
    ]
