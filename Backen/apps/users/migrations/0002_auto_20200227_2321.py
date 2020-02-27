# Generated by Django 3.0.2 on 2020-02-27 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='org',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.OrgProfile', verbose_name='机构号信息'),
        ),
    ]
