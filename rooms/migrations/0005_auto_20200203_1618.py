# Generated by Django 3.0.2 on 2020-02-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200203_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Room Type'},
        ),
        migrations.RemoveField(
            model_name='amenity',
            name='sub_title',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='sub_title',
        ),
        migrations.RemoveField(
            model_name='houserule',
            name='sub_title',
        ),
        migrations.RemoveField(
            model_name='roomtype',
            name='sub_title',
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
