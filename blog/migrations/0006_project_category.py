# Generated by Django 4.2.3 on 2023-08-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(to='blog.categorie'),
        ),
    ]