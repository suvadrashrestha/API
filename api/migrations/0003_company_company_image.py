# Generated by Django 5.0.6 on 2024-05-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_image',
            field=models.FileField(default=None, max_length=300, null=True, upload_to='company/'),
        ),
    ]
