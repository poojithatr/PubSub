# Generated by Django 3.2.7 on 2021-09-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBackend', '0007_alter_userdetail_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_email',
            field=models.CharField(default='user_email', max_length=20),
        ),
    ]
