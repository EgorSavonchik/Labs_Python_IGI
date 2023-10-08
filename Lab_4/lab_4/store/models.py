from django.db import models
from django.urls import reverse
from login.models import CustomUser
# Create your models here.

GRADLE_CHOICES = [(x, x * '★') for x in range (1, 6)]

class ProductType(models.Model) :
    
    name = models.CharField(max_length=200,
                             help_text='Enter product type')

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[str(self.name)])
    
    def __str__(self) :
        return self.name
    
class Producer(models.Model) :

    name = models.CharField(max_length=200,
                            help_text='Enter prodecer name')
    country = models.CharField(max_length=200,
                               help_text='Enter producer country')

    def get_absolute_url(self):
        return reverse('producer-detail', args=[str(self.id)])

    def __str__(self) :
        return self.name 
    
class Product(models.Model) :

    name = models.CharField(max_length=200)
    producer = models.ForeignKey('Producer',
                                    on_delete = models.SET_NULL,
                                    null = True)
    cost = models.IntegerField()
    type = models.ForeignKey('ProductType', 
                                on_delete = models.SET_NULL,
                                null = True)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    purchase_count = models.PositiveIntegerField(default=0)
    UNITS = (
        ('L', 'liter'),
        ('KG', 'kilogramm'),
        ('PC', 'pieces')
    )
    
    units = models.CharField(max_length=2,
                            choices=UNITS,
                            help_text="units of product")

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[str(self.id)])

    def __str__(self) :
        return self.name   
    
class Article(models.Model) :

    title = models.CharField(max_length=200,
                             help_text='Enter article title')
    short_argument = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='article')
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    def __str__(self) :
        return self.title
    
class Advertisement(models.Model) :

    adv_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='advertisement')
    link = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('advertisement-detail', args=[str(self.id)])

    def __str__(self) :
        return self.adv_name
    
class Partner(models.Model) :
    partner_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='partner')
    link = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('partner-detail', args=[str(self.id)])

    def __str__(self) :
        return self.partner_name
    
class Question(models.Model) :

    question = models.CharField(max_length=100)
    answer = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    def __str__(self) :
        return self.question
    
class WorkerInfo(models.Model) :

    worker = models.OneToOneField(CustomUser, on_delete=models.CASCADE, 
                               limit_choices_to={'is_staff': True})
    image = models.ImageField(upload_to="worker_info")
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('worker-info-detail', args=[str(self.id)])

    def __str__(self) :
        return '{0}, {1}'.format(self.worker.first_name, self.worker.last_name)
    
    class Meta:
        verbose_name_plural = 'Workers info'

class Vacancy(models.Model) :

    name = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    description = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('vacancy-detail', args=[str(self.id)])

    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name_plural = 'Vacancies'

class Review(models.Model) :

    title = models.CharField(max_length=200)
    gradle = models.PositiveIntegerField(choices=GRADLE_CHOICES)
    text = models.TextField(max_length=1000)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('review-detail', args=[str(self.id)])

    def __str__(self) :
        return self.title

class Coupon(models.Model) :

    discount = models.PositiveIntegerField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=50)
    active = models.BooleanField()

    def get_absolute_url(self):
        return reverse('coupon-detail', args=[str(self.id)])

    def __str__(self) :
        return '{0}, {1}'.format(self.date_of_creation, self.discount)
    
class History(models.Model) :

    year = models.IntegerField()
    event = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('history-detail', args=[str(self.id)])

    def __str__(self) :
        return '{0}, {1}'.format(self.year, self.event)
    
    class Meta:
        verbose_name_plural = 'History'