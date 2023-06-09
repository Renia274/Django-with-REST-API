from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)  # Name field for the category

    class Meta:
        db_table = 'categories_category'  # Database table name for the Category model

    def __str__(self):
        return self.name  # String representation of the Category model


# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)  # Name field for the product
    description = models.TextField()  # Description field for the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Foreign key relationship to Category model

    class Meta:
        app_label = 'products'  # App label for the Product model

    def __str__(self):
        return self.name  # String representation of the Product model

