from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from parler.models  import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations=TranslatedFields(
    name=models.CharField(verbose_name="نام",max_length=100,db_index=True),
    slug=models.SlugField(verbose_name="نام",db_index=True)
    )
    class Meta:
        verbose_name_plural="دسته بندی"
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product:item_product_view', kwargs={'slug': self.slug})
    # def __str__(self):
    #     return self.name
    
class Product(TranslatableModel):
    translations=TranslatedFields(
    name=models.CharField( max_length=256,db_index=True),
    price= models.PositiveIntegerField(),
    description = models.TextField(null=True, blank=True),
    slug=models.SlugField(db_index=True,null=True, blank=True) 
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    image = models.ImageField(upload_to='images/products/%Y%m%d', height_field=None)
    created_at = models.DateTimeField(auto_now_add=timezone.now, db_index=True)
    available=models.BooleanField(default=True)
    update_at=models.DateTimeField(auto_now=timezone.now,db_index=True)
    
    
    
    class  Meta:
        ordering=['-update_at','available','created_at']
        # index_together=['id','slug']
        
        #unique_together=['category','price']
        verbose_name_plural="محصولات"
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product:detail_item_view', kwargs={'id':self.id,'slug': self.slug})
    def __str__(self):
        return  f'{self.name}-----{self.price}'