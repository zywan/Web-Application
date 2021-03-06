# Generated by Django 2.1.2 on 2018-10-26 21:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtype', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for a project', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('ptype', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(help_text='Enter a user name', max_length=100)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for a user', primary_key=True, serialize=False)),
                ('email', models.EmailField(help_text='Enter a email address', max_length=254)),
                ('password', models.CharField(help_text='Enter the password', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vision.User'),
        ),
    ]
