from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True, validators=[
        MinLengthValidator(2),
        RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
    ], verbose_name='이름')
    description = models.TextField(verbose_name='소개')
    birth = models.CharField(max_length=100, verbose_name='생일')
    age = models.IntegerField(verbose_name='나이')
    height = models.IntegerField(verbose_name='키')
    hobby = models.CharField(max_length=100, verbose_name='취미')
    photo = models.ImageField(blank=True, verbose_name='사진')

    def __str__(self) -> str:
        return self.name