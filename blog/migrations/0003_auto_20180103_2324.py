# Generated by Django 2.0 on 2018-01-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_project_n_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='project',
            name='url_link',
            field=models.URLField(),
        ),
    ]
