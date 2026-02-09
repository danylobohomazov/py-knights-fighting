from app.knight import Knight


def knight_battle(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.battle(second_knight)
    second_knight.battle(first_knight)
