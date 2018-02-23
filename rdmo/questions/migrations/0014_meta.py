# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this catalog.', null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this catalog.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this question/questionset.', null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this question/questionset.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='subsection',
            field=models.ForeignKey(help_text='The subsection this question/questionset belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='questions.Subsection', verbose_name='Subsection'),
        ),
        migrations.AlterField(
            model_name='section',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this section.', null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='section',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this section.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=0, help_text='Position in lists.', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this subsection.', null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this subsection.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='order',
            field=models.IntegerField(default=0, help_text='Position in lists.', verbose_name='Order'),
        ),
    ]