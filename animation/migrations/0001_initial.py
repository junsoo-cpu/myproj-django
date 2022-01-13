# Generated by Django 3.2.11 on 2022-01-13 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('[ㄱ-힣]', message='한글을 입력해주세요.')], verbose_name='이름')),
                ('description', models.TextField(verbose_name='소개')),
                ('birth', models.DateField(verbose_name='생년월일')),
                ('age', models.IntegerField(verbose_name='나이')),
                ('height', models.IntegerField(verbose_name='키')),
                ('hobby', models.CharField(max_length=100, verbose_name='취미')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='사진')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]