# from django.db import models
#
# # Create your models here.
#
# class Tag(models.model): # 태그 모델
#     name = models.CharField(max_length=12)
#     value = models.FloatField()
#
# class Input(models.model): # 처음 입력 모델
#     user_id = models.OneToOneField(User, on_delete=models.CASCADE)
#     tag = models.ManyToManyField(Tag, blank=True)
#     period = models.IntegerField()
#     area = models.CharField(max_length=20)
#
# class Tour(models.model): # 관광지 모델
#     name = models.CharField(max_length=30)
#     '''관광지 이름, 콘텐츠 소요시간, 위치, etc...'''
#     pass
#
# class Restaurant(models.model): # 식당 모델
#     pass
#
# class Stay(models.model): # 숙소 모델
#     pass
#
# class Schedule(models.model): # 일정리스트 모델
#     user_id = models.OneToOneField(User, on_delete=models.CASCADE)
#     tag = models.ManyToManyField(Tag, blank=True)
#     tour = models.ManyToManyField(Tour, blank=True)
#     restaurant = models.ManyToManyField(Restaurant, blank=True)
#     stay = models.ManyToManyField(Stay, blank=True)
