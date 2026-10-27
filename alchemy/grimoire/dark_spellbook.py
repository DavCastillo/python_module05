from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eye-ball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validator = validate_ingredients(ingredients)
    if ("VALID" in validator):
        return (f"Spell recorded: {spell_name} {validator}")
    else:
        return (f"Spell rejected: {spell_name} {validator}")
