# Generated by Django 3.2.3 on 2021-05-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentPortal', '0004_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]
