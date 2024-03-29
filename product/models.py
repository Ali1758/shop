from django.db import models


class Category (models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def is_parent(self):
        if self.parent_category:
            return False
        return True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    off_percent = models.DecimalField(max_digits=4, decimal_places=2)
    off_expire = models.DateField()
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    sold = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    rate_count = models.PositiveIntegerField()
    fast_send = models.BooleanField(default=False)
    pic_size = models.ImageField(upload_to='pictures/products_size')
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'products'


class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures/{}/'.format(product.name))

    def __str__(self):
        return 'تصویر محصول - {}'.format(self.product.name)

    class Meta:
        verbose_name = 'picture'
        verbose_name_plural = 'pictures'
        db_table = 'pictures'


class Tag(models.Model):
    product = models.ManyToManyField(Product, 'product')
    tag = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.tag)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        db_table = 'tags'
