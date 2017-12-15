# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-15 03:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        ('account', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compensation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('value', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_taken', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
                ('client_dashboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='dashboard.Dashboard')),
                ('compensation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='project.Compensation')),
                ('freelancer_dashboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to='dashboard.Dashboard')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set([('project', 'task_number')]),
        ),
    ]
