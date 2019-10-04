from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    product_desc=models.CharField(max_length=1500)
    product_pub_data=models.DateField()
    product_catogery=models.CharField(max_length=50,default="")
    product_sub_catogery=models.CharField(max_length=50,default="")
    product_price=models.IntegerField(default=0)
    proudct_image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class CustomerQuery(models.Model):
    query_id=models.AutoField(primary_key=True)
    cust_name=models.CharField(max_length=100,default="")
    cust_phone=models.CharField(max_length=20,default="0")
    cust_email=models.CharField(max_length=100,default="")
    cust_query=models.CharField(max_length=5000,default="")

    def __str__(self):
        return self.cust_name

    
