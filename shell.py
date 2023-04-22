from app.models import *


c1 = Category.objects.create(name="products")
c2 = Category.objects.create(name="soap_washer")

Product.objects.create(name='bread', worth=20, category=c1)
Product.objects.create(name='water', worth=45, category=c1)

Product.objects.create(name='dish_detergent', worth=150, category=c2)
Product.objects.create(name='powder', worth=320, category=c2)
Product.objects.create(name='shampoo', worth=500, category=c2)
