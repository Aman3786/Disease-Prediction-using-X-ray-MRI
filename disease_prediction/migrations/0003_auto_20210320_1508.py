# Generated by Django 3.0.5 on 2021-03-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease_prediction', '0002_remove_post_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='disease_img/'),
        ),
        migrations.AddField(
            model_name='post_image',
            name='tagi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
