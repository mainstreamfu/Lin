# Generated by Django 2.2.2 on 2019-07-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20190701_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='creat_time',
            new_name='create_time',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=255, verbose_name='评论内容'),
        ),
    ]
