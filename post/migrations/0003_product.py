# Generated by Django 4.2.7 on 2023-11-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]