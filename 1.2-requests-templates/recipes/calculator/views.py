from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def get_omlet_recipe(request):
    # показывает список ингредиентов и их количество для приготовления омлета
    servings_number = int(request.GET.get('servings', 1))
    ingredients: dict = DATA['omlet']
    for ingredient, value in ingredients.items():
        ingredients[ingredient] = servings_number * value

    context = {
        'recipe': ingredients

    }
    return render(request, 'calculator/index.html', context)


def get_pasta_recipe(request):
    # показывает список ингредиентов и их количество для приготовления макарон
    servings_number = int(request.GET.get('servings', 1))
    ingredients: dict = DATA['pasta']
    for ingredient, value in ingredients.items():
        ingredients[ingredient] = servings_number * value

    context = {
        'recipe': ingredients

    }
    return render(request, 'calculator/index.html', context)


def get_buter_recipe(request):
    # показывает список ингредиентов и их количество для приготовления бутерброда
    servings_number = int(request.GET.get('servings', 1))
    ingredients: dict = DATA['buter']
    for ingredient, value in ingredients.items():
        ingredients[ingredient] = servings_number * value

    context = {
        'recipe': ingredients

    }
    return render(request, 'calculator/index.html', context)