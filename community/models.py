from django.db import models

# Create your models here.

class Tag(models.Model): # 태그 모델
    name = models.CharField(max_length=12)
    value = models.FloatField()

class User(models.Model): # 유저 모델
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS, default = '')
    tag = models.CharField(max_length=12, null=True)
    def __str__(self):
        return self.tag

class Input(models.Model): # 처음 입력 모델
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    startperiod = models.DateTimeField()
    endperiod = models.DateTimeField()
    area = models.CharField(max_length=20)
    def __str__(self):
        return self.tag

class Tour(models.Model): # 관광지 모델
    name = models.CharField(max_length=30)
    tourTime = models.IntegerField(null=True)
    tourLatitue = models.FloatField()
    tourLongitude = models.FloatField()
    tour_url = models.URLField('관광지 URL', max_length=400, blank=True,null=True,default='')
    image_file = models.ImageField('관광지 이미지', upload_to='tours', blank=True, null=True)
    '''관광지 이름, 콘텐츠 소요시간, 위치, etc...'''
    pass

class Restaurant(models.Model): # 식당 모델
    name = models.CharField(max_length = 20)
    restaurantTime = models.IntegerField(null=True)
    restaurantLatitue = models.FloatField()
    restaurantLognitude = models.FloatField()
    restaurant_url = models.URLField('식당 URL', max_length=400, blank=True,null=True,default='')
    image_file = models.ImageField('식당 이미지', upload_to='restaurants', blank=True, null=True)

    pass

class Stay(models.Model): # 숙소 모델
    name = models.CharField(max_length=20)
    stayLatitue = models.FloatField()
    stayLognitude = models.FloatField()
    restaurant_url = models.URLField('숙소 UR', max_length=400, blank=True,null=True, default='')
    image_file = models.ImageField('숙소 이미지', upload_to='stays', blank=True, null=True)

    pass


class Schedule(models.Model): # 일정리스트 모델
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    tour = models.ManyToManyField(Tour, blank=True)
    restaurant = models.ManyToManyField(Restaurant, blank=True)
    stay = models.ManyToManyField(Stay, blank=True)
