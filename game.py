


import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been eliminated!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        self.players.append(Player(name))

    def display_players(self):
        for player in self.players:
            print(player)

    def simulate_combat(self):
        while len([p for p in self.players if p.is_alive()]) > 1:
            attacker = random.choice(self.players)
            defender = random.choice([p for p in self.players if p != attacker and p.is_alive()])
            damage = random.randint(10, 30)

            print(f"{attacker.name} attacks {defender.name} for {damage} damage.")
            defender.take_damage(damage)

            # Удаляем мёртвых игроков
            self.players = [p for p in self.players if p.is_alive()]

        # Определяем победителя
        winner = self.players[0] if self.players else None
        if winner:
            print(f"{winner.name} is the winner!")
        else:
            print("No winners this time!")


if __name__ == "__main__":
    game = Game()

    # Добавляем игроков
    game.add_player("Player 1")
    game.add_player("Player 2")
    game.add_player("Player 3")

    # Показываем текущих игроков
    print("Current Players:")
    game.display_players()

    # Начинаем бой
    print("\nCombat begins!")
    game.simulate_combat()


