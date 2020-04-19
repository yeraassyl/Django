# Generated by Django 3.0.5 on 2020-04-19 18:23

from django.db import migrations, models
import todo.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200419_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='todolist', validators=[todo.main.validators.validate_file_size, todo.main.validators.validate_extension]),
        ),
    ]
