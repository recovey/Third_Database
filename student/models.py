from django.db import models
from datetime import datetime


# 模型类必须要直接或者间接继承于 models.Model
class BaseModel(models.Model):
    """公共模型[公共方法和公共字段]"""
    # created_time = models.IntegerField(default=0, verbose_name="创建时间")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # auto_now_add 当数据添加时设置当前时间为默认值
    # auto_now= 当数据添加/更新时, 设置当前时间为默认值
    updated_time = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True  # 设置当前模型为抽象模型, 当系统运行时, 不会认为这是一个数据表对应的模型.


class Student(BaseModel):
    """Student模型类"""
    # 1. 字段[数据库表字段对应]
    SEX_CHOICES = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )

    # 字段名 = models.数据类型(约束选项1,约束选项2, verbose_name="注释")
    # SQL: id bigint primary_key auto_increment not null comment="主键",
    # id = models.AutoField(primary_key=True, null=False, verbose_name="主键") # django会自动在创建数据表的时候生成id主键/还设置了一个调用别名 pk

    # SQL: name varchar(20) not null comment="姓名"
    # SQL: key(name),
    name = models.CharField(max_length=20, db_index=True, verbose_name="姓名")

    # SQL: age smallint not null comment="年龄"
    age = models.SmallIntegerField(verbose_name="年龄")

    # SQL: sex tinyint not null comment="性别"
    # sex = models.BooleanField(verbose_name="性别")
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=2)

    # SQL: class varchar(5) not null comment="班级"
    # SQL: key(class)
    classmate = models.CharField(db_column="class", max_length=5, db_index=True, verbose_name="班级")
    # SQL: description longtext default "" not null comment="个性签名"
    description = models.TextField(default=None, null=True, verbose_name="个性签名")

    # 2. 数据表结构信息
    class Meta:
        db_table = 'tb_student'  # 指明数据库表名,如果没有指定表明,则默认为子应用目录名_模型名称,例如: users_student
        verbose_name = '学生信息表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    # 3. 自定义数据库操作方法
    def __str__(self):
        """定义每个数据对象的显示信息"""
        return "<User %s>" % self.name


# def student(Model):
#     name = models.CharField(max_length=20, db_index=True, verbose_name="姓名")
#     age = models.CharField(verbose_name="年龄")
#     sex = models.SmallIntegerField(verbose_name="年龄")
#     classmate = models.CharField(db_column="class", max_length=5, db_index=True, verbose_name="班级")
#     description = models.TextField(default="", verbose_name="个性签名")
#     created_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
#     updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#
#     class Mate:
#         db_table = "db_student"
#         verbose_name = "学生信息表"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return f"<User {self.name}>"
