from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_list = ingredients.replace(" and ", ",").split(",")
    for ingredient in ingredients_list:
        if ingredient.strip() in allowed:
            return (f"({ingredients} - VALID)")
    return (f"({ingredients} - INVALID)")
