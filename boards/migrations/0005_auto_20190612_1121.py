# Generated by Django 2.2.2 on 2019-06-12 11:21

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_board_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='boards/images'),
        ),
    ]
