from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    author = models.CharField(max_length=100, verbose_name='Напишите имя автора')
    description = models.TextField(verbose_name='Напишите описание', blank=True)
    image = models.ImageField(upload_to='book/', verbose_name='Загрузите фото', blank=True)
    # book_file = models.FileField(upload_to='book/', verbose_name='Загрузите файл', blank=True)
    GENRE = (
        ('Альтернативная история', 'Альтернативная история'),
        ('Антиутопия', 'Антиутопия'),
        ('Биография', 'Биография'),
        ('Боевик', 'Боевик'),
        ('Детский', 'Детский'),
        ('Драма', 'Драма'),
        ('Комедия', 'Комедия'),
        ('Криминал', 'Криминал'),
        ('Научная фантастика', 'Научная фантастика'),
        ('Научный', 'Научный'),
        ('Ужас', 'Ужас'),
        ('Фэнтези', 'Фэнтези')
    )
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр', default='Детский', blank=True, null=True)
    pages = models.PositiveIntegerField(verbose_name='Укажите кол-во страниц', default=20, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Укажите цену', default=100, blank=True, null=True)
    published_date = models.PositiveIntegerField(verbose_name='Укажите год издания книги', default=2000, blank=True, null=True)
    language = models.CharField(max_length=30, verbose_name='Укажите язык книги', default='Русский', blank=True, null=True)
    isbn = models.CharField(max_length=20, verbose_name='Укажите ISBN', default="0", blank=True,  null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Create your models here.
