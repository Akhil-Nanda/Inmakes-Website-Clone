# Generated by Django 4.1.7 on 2023-07-01 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Levelperprogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.internshipprograms')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdetails.level')),
            ],
        ),
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_name', models.CharField(max_length=250)),
                ('contents', models.FileField(upload_to='program_videos/')),
                ('level_per_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdetails.levelperprogram')),
            ],
        ),
    ]