# Generated by Django 4.2.7 on 2023-11-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_animal_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
