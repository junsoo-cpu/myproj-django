from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(TimestampedModel):
    title = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(3),
            RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
        ],
    )
    content = models.TextField()
    photo = models.ImageField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title
