# Generated by Django 2.1.7 on 2019-02-16 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(blank=True, help_text='eg: Poornima College Of Engineering, Jaipur', max_length=100)),
                ('branch', models.CharField(choices=[(1, 'Computer Science Engineering'), (2, 'Electronics and Communication Engineering'), (3, 'Electrical engineering'), (4, 'Mechanical Engineering'), (5, 'Information Technology Engineering'), (6, 'Civil Engineering'), (7, 'Chemical Engineering'), (8, 'Aeronautical Engineering'), (9, 'Agricultural engineering'), (10, 'Mining engineering'), (11, 'Biochemical engineering'), (12, 'Electrical and Instrumentation Engineering'), (13, 'Metallurgical Engineering')], default=1, max_length=50)),
                ('mobile', models.CharField(blank=True, help_text='Enter your 10-digit Mobile Number', max_length=10, null=True)),
                ('cc_points', models.IntegerField(default=0)),
                ('user', models.OneToOneField(help_text='eg: johndoe101', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]