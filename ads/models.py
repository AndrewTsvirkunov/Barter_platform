from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок объявления', max_length=225)
    description = models.TextField('Описание товара')
    image_url = models.URLField('URL изображения', blank=True, null=True)
    category = models.CharField('Категория товара', max_length=100)
    condition = models.CharField('Состояние товара', max_length=50)  # например: "новый", "б/у"
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class ExchangeProposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('accepted', 'Принята'),
        ('declined', 'Отклонена')
    ]

    ad_sender = models.ForeignKey(Ad, related_name='sent_proposals', on_delete=models.CASCADE)
    ad_receiver = models.ForeignKey(Ad, related_name='received_proposal', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Предлагается обменять {self.ad_sender} на {self.ad_receiver}."

    class Meta:
        verbose_name = 'Предложение обмена'
        verbose_name_plural = 'Предложения обмена'