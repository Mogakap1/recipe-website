from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_list(request):
    """View to display all recipes with filtering and search"""
    category = request.GET.get('category')
    search = request.GET.get('search')
    
    recipes = Recipe.objects.all()
    
    # Filter by category if specified
    if category:
        recipes = recipes.filter(category=category)
    
    # Search by title if specified
    if search:
        recipes = recipes.filter(title__icontains=search)
    
    context = {
        'recipes': recipes,
        'selected_category': category,
        'search_query': search,
    }
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, pk):
    """View to display a single recipe"""
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
