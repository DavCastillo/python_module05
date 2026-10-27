import alchemy.grimoire as grimoire


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validator = grimoire.validate_ingredients(ingredients)
    if ("VALID" in validator):
        return (f"Spell recorded: {spell_name} {validator}")
    else:
        return (f"Spell rejected: {spell_name} {validator}")
