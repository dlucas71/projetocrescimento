# Generated by Django 2.1 on 2018-09-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/imgs', verbose_name='Imagem'),
        ),
    ]