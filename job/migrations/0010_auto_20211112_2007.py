# Generated by Django 3.2.9 on 2021-11-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_application_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='application',
            name='website',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
