# Generated by Django 3.2.7 on 2021-09-27 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBackend', '0004_alter_userdetail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
