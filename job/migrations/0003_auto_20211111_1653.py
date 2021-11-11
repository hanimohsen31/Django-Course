# Generated by Django 3.2.9 on 2021-11-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_jobtype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='jobtype',
            new_name='job_type',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]