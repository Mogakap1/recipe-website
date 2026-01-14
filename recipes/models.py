from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('desserts', 'Desserts'),
        ('vegetarian', 'Vegetarian'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cooking_time = models.IntegerField(help_text="Time in minutes")
    servings = models.IntegerField()
    ingredients = models.TextField(help_text="Enter each ingredient on a new line")
    instructions = models.TextField(help_text="Enter cooking instructions, one step per line")
    emoji = models.CharField(max_length=10, default="🍽️", help_text="Emoji for the recipe")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_ingredients_list(self):
        """Return ingredients as a list"""
        return [ing.strip() for ing in self.ingredients.split('\n') if ing.strip()]
    
    def get_instructions_list(self):
        """Return instructions as a list"""
        return [inst.strip() for inst in self.instructions.split('\n') if inst.strip()]