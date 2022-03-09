from django.db import models

# Create your models here.分类
class Type(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name
# 游戏信息
class Game(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default='0')
    name = models.CharField(max_length=128)
    info = models.CharField(max_length=256)
    likes = models.IntegerField(default='0')
    pic = models.ImageField(upload_to='image', default='image/1.jpg')
    time = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.name
