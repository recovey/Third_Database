# Generated by Django 3.2.9 on 2021-11-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classmate',
        ),
        migrations.AddField(
            model_name='student',
            name='class_number',
            field=models.IntegerField(db_column='class', null=True, verbose_name='班级'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.SmallIntegerField(default=0, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='个性签名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(db_index=True, max_length=20, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.SmallIntegerField(choices=[(0, '女'), (1, '男'), (2, '保密')], default=0, null=True, verbose_name='性别'),
        ),
    ]
