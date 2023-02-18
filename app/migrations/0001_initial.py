# Generated by Django 3.0 on 2023-02-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('birthdate', models.DateField()),
                ('gender', models.TextField(max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]