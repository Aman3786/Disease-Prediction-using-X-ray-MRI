# Generated by Django 3.0.5 on 2021-04-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorinfo',
            name='image',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
