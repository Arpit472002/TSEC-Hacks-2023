# Generated by Django 4.1.6 on 2023-02-02 13:33

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_myuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='interests',
            field=django_mysql.models.ListCharField(models.CharField(max_length=255), blank=True, max_length=255, null=True, size=None),
        ),
    ]
