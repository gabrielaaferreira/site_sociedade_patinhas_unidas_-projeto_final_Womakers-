# Generated by Django 4.2.7 on 2023-11-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_animal_options_animal_id_ficha'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='foto',
            field=models.ImageField(default='richard.jpg', upload_to='static/img'),
        ),
    ]
