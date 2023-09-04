# Generated by Django 3.2.7 on 2021-09-27 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppBackend', '0002_alter_userdetail_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='name',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='interest',
            field=models.CharField(max_length=30),
        ),
    ]
