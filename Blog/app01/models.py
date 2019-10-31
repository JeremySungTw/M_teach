from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name="店名")
    phone = models.CharField(max_length=255, verbose_name="電話")
    address = models.CharField(max_length=255, verbose_name="地址", blank=True, null=True)
    delivery = models.PositiveIntegerField(verbose_name="外送金額", blank=True, null=True)
    menu_pic = models.CharField(max_length=255, verbose_name="菜單圖片", blank=True, null=True)
    eva = models.PositiveIntegerField(verbose_name="評價", blank=True, null=True)
    url = models.URLField(unique=True, blank=True, null=True)
    black_list = models.BooleanField(default=False, verbose_name="黑名單")
    type = models.ManyToManyField('Type', blank=True)

    # superuser Return Obj
    def __str__(self):
        return "%s %s" % (self.name, self.phone)


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name="菜名")
    price = models.IntegerField(verbose_name="價格")
    info = models.CharField(max_length=255, verbose_name="詳細資訊", blank=True, null=True)
    custom = models.ManyToManyField('Custom', verbose_name="客製化", blank=True, null=True)
    menuName = models.ForeignKey('Shop')

    def __str__(self):
        return self.name


# 菜品客製項目
class Custom(models.Model):
    name = models.CharField(max_length=255, verbose_name="訂製名稱")

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name="類型名稱")

    def __str__(self):
        return self.name

# 訂購單
class Order(models.Model):
    initiator = models.CharField(max_length=255, verbose_name="發起人")
    release_date = models.DateField(verbose_name="訂購日期")
    deadline_date = models.DateField(verbose_name="截止日期", blank=True, null=True)
    info = models.CharField(max_length=255, verbose_name="訂單備註", blank=True, null=True)
    shop = models.ForeignKey("Shop")

    def __str__(self):
        return "%s Shop: %s" % (self.id, self.shop)

# 訂單內容 1
class Orderdetail(models.Model):
    number = models.ForeignKey("Order")
    orderer = models.CharField(max_length=255, verbose_name="訂購人")
    ordermune = models.ManyToManyField("Orderitem")

    def __str__(self):
        return "%s %s %s" % (self.number.id, self.orderer, self.number.shop )

class Orderitem(models.Model):
    product = models.ForeignKey("Menu")
    quantity = models.IntegerField(verbose_name="餐點數量")
    info = models.CharField(max_length=255, verbose_name="餐點備註", blank=True, null=True)

    def __str__(self):
        return "%s" % (self.product.name)