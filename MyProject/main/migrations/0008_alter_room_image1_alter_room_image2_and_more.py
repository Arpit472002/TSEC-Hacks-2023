# Generated by Django 4.1.6 on 2023-02-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_interested_users_room_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='panaroma_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
