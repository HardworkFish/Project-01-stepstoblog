# Generated by Django 2.0.5 on 2018-08-23 09:04

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180823_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True, verbose_name='详细内容'),
        ),
    ]
