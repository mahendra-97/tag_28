# Generated by Django 4.1.5 on 2023-12-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_api', '0010_alter_tagsmodel_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagsmodel',
            name='scope',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='scope'),
        ),
    ]