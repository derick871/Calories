from django.db import models

class Client(models.Model):
    # Expanded max_length to safely accommodate standard email lengths
    email = models.EmailField(max_length=255, unique=True)
    # Increased max_length to 128 to properly support hashed passwords if needed
    password = models.CharField(max_length=128) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Subscriber(models.Model):
    # Changed 'Unique' to lowercase 'unique'
    email = models.EmailField(max_length=255, unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class FoodItem(models.Model):
    """
    Model to handle food logging and calorie tracking metrics.
    """
    name = models.CharField(max_length=100)
    calories = models.FloatField(help_text="Energy content in kcal")
    protein = models.FloatField(default=0.0, help_text="Protein in grams (g)")
    carbs = models.FloatField(default=0.0, help_text="Carbohydrates in grams (g)")
    fats = models.FloatField(default=0.0, help_text="Fats in grams (g)")
    
    # Optional: Link the food item to a client tracker profile
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="logged_foods", null=True, blank=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"