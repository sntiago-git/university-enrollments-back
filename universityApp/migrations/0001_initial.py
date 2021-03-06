# Generated by Django 3.2.8 on 2021-10-08 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
                ('lastname', models.CharField(max_length=45, verbose_name='Lastname')),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
                ('gender', models.CharField(max_length=15, verbose_name='Gender')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(max_length=20, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=15, verbose_name='Name')),
                ('short_desc', models.TextField(max_length=45, verbose_name='Short_desc')),
                ('long_desc', models.TextField(max_length=300, verbose_name='Long_desc')),
                ('schedule', models.TextField(max_length=300, verbose_name='Schedule')),
                ('semester', models.CharField(max_length=20, verbose_name='Semester')),
                ('credits', models.IntegerField(verbose_name='Credits')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
                ('lastname', models.CharField(max_length=45, verbose_name='Lastname')),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
                ('gender', models.CharField(max_length=15, verbose_name='Gender')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='universityApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='universityApp.teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universityApp.career'),
        ),
        migrations.AddField(
            model_name='student',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='student',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
