# Generated by Django 3.1.4 on 2020-12-29 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_counsellor_faculty_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='counsellor',
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
