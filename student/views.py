from django.http.response import HttpResponse
from django.views import View

from .models import Student


# Create your views here.


def index(request):
    return HttpResponse("<h1>登录成功</h1>")


class BaseDBView(View):
    """数据库基本操作"""

    def get(self, request):
        """查询数据"""
        # 1.通过get获取一条数据
        # try:
        #     student = Student.objects.get(name="刘德华")
        #     print(student)
        #     print(student.description)
        # except Student.MultipleObjectsReturned:
        #     print("查询得到多个结果")
        # except Student.DoesNotExist:
        #     print("查询结果不存在")

        # 2.基于first查询第一条数据
        # # 没有结果返回None,有结果返回第一个
        # student = Student.objects.filter(name="刘德华").first()
        # print(student.id)

        # 3.all获取多条记录
        # # 等到结果,已QuerySet结果返回,没有结果则返回空列表
        # student_lst = Student.objects.filter(id=1).all()
        # '''
        # <QuerySet [<Student: <User 刘德华>>, <Student: <User 刘德华>>]>
        # '''
        # # QuerySet 是继承list的一个类
        # print(student_lst)

        # 4.count统计数量
        ret = Student.objects.filter(name="刘德华").count()
        print(ret)
        return HttpResponse("ok")

    def post(self, request):
        """添加数据"""
        # # 方法1：基于save方法添加一条数据，先实例化对象，然后通过对象调用save方法进行保存添加
        # student = Student(name="刘德华", age=14, sex=True, classmate=301, description="一杯忘情水。")
        # # 保存数据
        # student.save()
        # print(student.id)  # 如果返回none则执行失败
        # 方法2：基于create添加数据
        student = Student.objects.create(name="刘德华", age=14, sex=True, classmate=301, description="一杯忘情水。")
        print(student.id)

        return HttpResponse("ok")

    def put(self, request):
        """修改方法"""
        # # 方法1
        # student = Student.objects.filter(name="刘德华").first()
        # print(student)
        # student.age = 30
        # student.name = "张三"
        # student.save()
        # 方法2
        student = Student.objects.filter(name="刘德华").update(name="李四")
        print(student)
        return HttpResponse("ok")

    def delete(self, request):
        # 方法1
        # student = Student.objects.filter(name="张三").first()
        # student.delete()
        Student.objects.filter(name="李四").first().delete()
        return HttpResponse("ok")


class DBView(View):
    # 基础查询
    # def get(self, request):
    #     student = Student.objects.filter(classmate=301).all()
    #     print(student)
    #     for s in student:
    #         print(s)
    #     return HttpResponse("ok")
    # 模糊查询
    # def get(self, request):
    #     # 查询以张开头的名字
    #     student = Student.objects.filter(name__startswith="张").all()
    #     print(student)
    #     # 查询以华结尾的名字
    #     student = Student.objects.filter(name__endswith="华").all()
    #     print(student)
    #     # 查询包含华字的同学
    #     student = Student.objects.filter(name__contains="华").all()
    #     print(student)
    #     # 查询出有没有叫杜文华的同学，没有返回空列表
    #     student = Student.objects.filter(name__iexact="杜文华").all()
    #     print(student)
    #     return HttpResponse("ok")
    # 空查询
    # def get(self, request):
    #     # 查询出字段description是空的所有学生
    #     student = Student.objects.filter(description__isnull=True).all()
    #     print(student)
    #     return HttpResponse("ok")
    # 范围查询
    # def get(self, request):
    #     # 查询出401-404的所有学生
    #     student = Student.objects.filter(classmate__in=[401, 402, 403, 404]).all()
    #     print(student)
    #     print(len(student))
    #     return HttpResponse("ok")
    # 比较查询
    # def get(self, request):
    #     # 大于 age__get = 19 ==> age > 19
    #     student = Student.objects.filter(age__gt=19).all()
    #     print(student)
    #     print(len(student))
    #     # 小于 lt 小于等于lte
    #     student = Student.objects.filter(age__lt=19).all()
    #     print(student)
    #     print(len(student))
    #     return HttpResponse("ok")
    # 时间查询
    # def get(self, request):
    #     # 查询2018年被添加到数据库中学生
    #     student = Student.objects.filter(created_time__year=2018)
    #     print(student)
    #     # 查询2019年5月20号被添加进来的同学
    #     from django.utils import timezone as datetime
    #     student = Student.objects.filter(created_time__gte=datetime.datetime(2019, 5, 20),
    #                                      created_time__lt=datetime.datetime(2019, 5, 21)).all()
    #     print(student)
    #     return HttpResponse("ok")
    # F 查询
    # def get(self, request):
    #     # 查询添加时间与修改时间相同的学生
    #     from django.db.models import F
    #     student = Student.objects.filter(created_time=F("updated_time"))
    #     print(student)
    #     print(len(student))
    #     return HttpResponse("ok")
    # Q 查询
    # def get(self, request):
    #     # 查询出年龄大于20岁或者年龄小于18岁的学生
    #     from django.db.models import Q
    #     student = Student.objects.filter(Q(age__lt=18) | Q(age__gt=20))
    #     print(student)
    #     print(len(student))
    #     return HttpResponse("ok")
    # 结果排序
    # def get(self, request):
    #     # 查询出301班所有学生并且按年龄的升序和降序分别排序
    #     # order_by("字段") : 相当于asc  从小到大
    #     # order_by("-字段") : 相当于desc  从大到小
    #     # student_list = Student.objects.filter(classmate=301).order_by("-age").all()
    #     student_list = Student.objects.filter(classmate=301).order_by("age").all()  # 正序
    #     for student in student_list:
    #         print(f"姓名:{student.name},年龄:{student.age}")
    #     return HttpResponse("ok")
    # QuerySet查询集
    def get(self, request):
        # 查询出301班是否有男生
        student = Student.objects.filter(classmate=301)
        student = student.order_by("-age")
        student = student.filter(sex=1)
        print(student)
        ret1 = student.values()  # 默认把所有字段全部转换返回
        print(ret1)
        ret2 = student.values("id", "name", "age")  # 可以通过参数设置要转换的字段并返回
        print(ret2)
        ret3 = student.values_list()  # 默认把所有字段全部转换返回
        print(ret3)
        ret4 = student.values_list("id", "name", "age")  # 可以通过参数设置要转换的字段并返回
        print(ret4)
        return HttpResponse("ok")


