from django.db import models


# Create your models here.
class PassportManager(models.Manager):
    # 添加账户信息
    def add_one_passport(self, username, password, email):
        passport = self.create(username=username, password=password, email=email)

    def get_one_passport(self, username, password):
        try:
            passport = self.get(username=username, password=password)
        # 如果找不到则返回用户不存在
        except self.model.DoesNotExist:
            passport = None
        return passport


# 用户信息表
class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=50, verbose_name="密码")
    gender = models.CharField(max_length=50, default=0, null=True, verbose_name="性别")
    phone = models.CharField(max_length=50, default="", null=True, verbose_name="手机号")
    email = models.EmailField(max_length=200, default="", null=True, verbose_name="邮箱")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 电子证照信息
    # img_img = models.CharField(max_length=50, default="", null=True, verbose_name="图片信息")
    # 后台管理页面上传图片
    img_url = models.ImageField(upload_to='img', default="", verbose_name='图片路径')
    img_gender = models.CharField(max_length=50, default="", verbose_name='图片上性别')
    img_name = models.CharField(max_length=50, default="", null=True, verbose_name="真实姓名")
    img_addr = models.CharField(max_length=200, default="", null=True, verbose_name="籍贯")
    img_sfz = models.CharField(max_length=200, default="", null=True, verbose_name="身份证号")

    STATUS_CHOICES = (
        ('未通过', '未通过'),
        ('通过', '通过'),
    )
    # 管理员审核状态码
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='未通过', verbose_name="审核状态")
    # 通行证管理
    objects = PassportManager()

    def __str__(self):
        return self.username + '-' + self.status

    class Meta:
        db_table = "user_info"
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class Yyzz(models.Model):
    user = models.OneToOneField(User, related_name="yyzz_user")
    img_url = models.ImageField(upload_to='img', default="", null=True, verbose_name='图片路径')
    dwmc = models.CharField(max_length=200, default="", null=True, verbose_name='单位名称')
    fr = models.CharField(max_length=200, default="", null=True, verbose_name="法人")
    dz = models.CharField(max_length=200, default="", null=True, verbose_name="地址")
    clrq = models.CharField(max_length=200, default="", null=True, verbose_name="成立日期")
    jyfw = models.CharField(max_length=500, default="", null=True, verbose_name="经营范围")
    lx = models.CharField(max_length=200, default="", null=True, verbose_name="类型")
    yxq = models.CharField(max_length=200, default="", null=True, verbose_name="有效期")
    zcxs = models.CharField(max_length=200, default="", null=True, verbose_name="组成形式")
    zjbh = models.CharField(max_length=200, default="", null=True, verbose_name="证件编号")
    shxydm = models.CharField(max_length=200, default="", null=True, verbose_name="社会信用代码")
    zczb = models.CharField(max_length=200, default="", null=True, verbose_name="注册资本")
    STATUS_CHOICES = (
        ('未通过', '未通过'),
        ('通过', '通过'),
    )
    # 管理员审核状态码
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='未通过', verbose_name="审核状态")


    def __str__(self):
        return self.dwmc + '-' + self.fr

    class Meta:
        db_table = "yyzz_info"
        verbose_name = '营业执照信息'
        verbose_name_plural = verbose_name
