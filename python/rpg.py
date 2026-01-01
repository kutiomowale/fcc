#!/usr/bin/env python3
full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if any(char.isspace() for char in name):
        return "The character name should not contain spaces"
    if any(
         not isinstance(stat, int)
         for stat in (strength, intelligence, charisma)
    ):
        return "All stats should be integers"
    if any(stat < 1 for stat in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"
    if ((strength + intelligence + charisma) != 7):
        return "The character should start with 7 points"

    line1 = name + '\n'
    line2 = (
        "STR "
        f"(full_dot * strength)"
        f"(empty_dot * (10 - strength))\n"
    )
    line3 = (
        "INT "
        f"(full_dot * intelligence) + (empty_dot * (10 - intelligence))"
        f"\n"
        )
    line4 = "CHA " + (full_dot * charisma) + (empty_dot * (10 - charisma))
    return line1 + line2 + line3 + line4
