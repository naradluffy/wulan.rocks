# Generated by Django 2.0 on 2018-01-15 02:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180105_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
