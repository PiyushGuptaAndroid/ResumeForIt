# Generated by Django 2.2.1 on 2021-05-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPortal', '0003_alter_question_correctoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]