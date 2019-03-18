# Generated by Django 2.1.7 on 2019-03-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20190316_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, help_text='Describe yourself, helps to connect with like-minded people.'),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.URLField(blank=True, help_text='Showcase your projects through this. \\n Your link to Github profile. eg: https://www.github.com/devaljain1998'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.URLField(blank=True, help_text='Showcase your professional profile through this. \\n Your link to LinkedIn profile. eg: https://www.linkedin.com/in/deval-sethi-00a2912a/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, 'Beginner'), (2, 'Bronze'), (3, 'Silver'), (4, 'Gold')], default=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(choices=[('Computer Science Engineering', 'Computer Science Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical engineering', 'Electrical engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Information Technology Engineering', 'Information Technology Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Aeronautical Engineering', 'Aeronautical Engineering'), ('Agricultural engineering', 'Agricultural engineering'), ('Mining engineering', 'Mining engineering'), ('Biochemical engineering', 'Biochemical engineering'), ('Electrical and Instrumentation Engineering', 'Electrical and Instrumentation Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year'), ('Fifth Year', 'Fifth Year'), ('Passout', 'Passout')], default=1, help_text='Your current year', max_length=20),
        ),
    ]
