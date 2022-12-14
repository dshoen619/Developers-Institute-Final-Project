# Generated by Django 4.1 on 2022-09-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testudo_app', '0012_savedcourses_a'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSavedCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('course_id', models.CharField(max_length=500)),
                ('semester', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('dept_id', models.CharField(blank=True, max_length=500, null=True)),
                ('department', models.CharField(blank=True, max_length=500, null=True)),
                ('credits', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('grading_method', models.CharField(blank=True, max_length=1000, null=True)),
                ('gen_ed', models.CharField(blank=True, max_length=1000, null=True)),
                ('core', models.CharField(blank=True, max_length=1000, null=True)),
                ('relationships', models.CharField(blank=True, max_length=3000, null=True)),
                ('sections', models.CharField(blank=True, max_length=3000, null=True)),
            ],
        ),
    ]
