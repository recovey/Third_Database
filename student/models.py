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
    # django的ORM会自动生成一个整型的主键,默认自增长,非空!所以在django中创建模型是不需要声明主键的,除非主键不是整型.或者非自增长
    # 一旦开发者声明了AutoField(primary_key=True)主键字段,则django就不会自动生成主键字段.
    name = models.CharField(max_length=20, db_index=True, null=True, verbose_name='姓名')
    age = models.SmallIntegerField(default=0, null=True, verbose_name='年龄')
    # sex  = models.BooleanField(default=True, verbose_name="性别")
    sex = models.SmallIntegerField(choices=SEX_CHOICES, null=True, default=0, verbose_name="性别")
    class_number = models.IntegerField(db_column="class", null=True, verbose_name='班级')
    description = models.TextField(default="", null=True, verbose_name='个性签名')

    # 2. 数据表结构信息
    class Meta:
        db_table = 'tb_student'  # 指明数据库表名,如果没有指定表明,则默认为子应用目录名_模型名称,例如: users_student
        verbose_name = '学生信息表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    # 3. 自定义数据库操作方法
    def __str__(self):
        """定义每个数据对象的显示信息"""
        return "<User(%s) %s[年龄:%s]>" % (self.pk, self.name, self.age)


class StudentInfo(BaseModel):
    """学生信息附加表"""
    # on_delete= 关联关系的设置

    # models.CASCADE    删除主键以后, 对应的外键所在数据也被删除
    # models.DO_NOTHING 删除主键以后, 对应的外键不做任何修改
    # 反向查找字段 related_name
    # 通过info查找学生信息, StudentInfo.student
    # 通过学生信息查找info, Student.info
    student = models.OneToOneField(Student, related_name="info", on_delete=models.DO_NOTHING, null=True)
    address = models.CharField(max_length=255, verbose_name="家庭地址")

    class Meta:
        db_table = 'tb_student_info'
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name


class Achievement(BaseModel):
    """成绩表"""
    student = models.ForeignKey(Student, related_name="score_list", on_delete=models.CASCADE, null=True)
    # max_digits 总数值长度[有多少个字符,不包含小数点]
    # decimal_places 小数位数值的字符最多允许有几个
    score = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="成绩")

    class Meta:
        db_table = 'tb_achievement'
        verbose_name = '学生成绩表'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    name = models.CharField(max_length=15, verbose_name="老师")

    class Meta:
        db_table = "tb_teacher"
        verbose_name = '老师信息表'
        verbose_name_plural = verbose_name


class Course(models.Model):
    name = models.CharField(max_length=15, verbose_name="课程")
    teacher_list = models.ManyToManyField(Teacher, related_name="course_list")

    class Meta:
        db_table = "tb_course"
        verbose_name = '老师信息表'
        verbose_name_plural = verbose_name


class Area(models.Model):
    """行政区划"""
    # 注意，django会自动创建主键，并默认字段名为：id
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self',on_delete=models.DO_NOTHING, blank=True, null=True, related_name="son_list")

    def __str__(self):
        return f"<Area> {self.name}"
