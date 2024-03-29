# Generated by Django 5.0.1 on 2024-02-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='title',
        ),
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='first_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='last_name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='mobile',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
