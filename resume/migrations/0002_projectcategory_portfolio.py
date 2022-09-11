# Generated by Django 4.0.5 on 2022-09-11 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.TextField(blank=True, default='#', max_length=2000, null=True)),
                ('project_image1', models.ImageField(blank=True, null=True, upload_to='project_img/')),
                ('project_desc', models.TextField(max_length=5000)),
                ('client', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.ImageField(default=999, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.projectcategory')),
            ],
        ),
    ]
