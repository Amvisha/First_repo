import pygame
import random
import math
import os

# Ініціалізація Pygame
pygame.init()

# Налаштування екрана
WIDTH, HEIGHT = 1280, 1024
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Танки 2025")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Завантаження зображень
def load_image(name):
    """Завантажує зображення та повертає об'єкт Surface."""
    fullname = os.path.join("images", name)  # Шлях до зображення
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image
    except pygame.error as e:
        print(f"Не вдалося завантажити зображення {name}: {e}")
        raise SystemExit

# Завантаження всіх зображень
player_image = load_image("player.png")  # Зображення гравця
enemy_image = load_image("enemy.png")    # Зображення ворога
bullet_image = load_image("bullet.png")  # Зображення кулі

# Гравці та вороги
class Player:
    def __init__(self):  # Виправлено на __init__
        self.health = 100
        self.position = [WIDTH // 2, HEIGHT // 2]
        self.angle = 0  # Кут повороту гравця
        self.speed = 5
        self.recoil = 0  # Ефект віддачі
        self.image = player_image
        self.rect = self.image.get_rect(center=self.position)

    def move(self, direction):
        if direction == "forward":
            self.position[0] += self.speed * math.cos(math.radians(self.angle))
            self.position[1] += self.speed * math.sin(math.radians(self.angle))
        elif direction == "backward":
            self.position[0] -= self.speed * math.cos(math.radians(self.angle))
            self.position[1] -= self.speed * math.sin(math.radians(self.angle))
        elif direction == "left":
            self.angle -= 5
        elif direction == "right":
            self.angle += 5

    def apply_recoil(self):
        # Віддача зсуває гравця назад
        recoil_strength = 8  # Сила віддачі
        self.position[0] -= recoil_strength * math.cos(math.radians(self.angle))
        self.position[1] -= recoil_strength * math.sin(math.radians(self.angle))
        self.recoil = recoil_strength

    def update_recoil(self):
        # Поступово зменшуємо ефект віддачі
        if self.recoil > 0:
            self.recoil -= 1

    def draw(self, screen):
        # Поворот зображення гравця
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        new_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, new_rect.topleft)

class Enemy:
    def __init__(self):  # Виправлено на __init__
        self.health = 50
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        self.image = enemy_image
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


class Bullet:
    def __init__(self, position, angle):  # Виправлено на __init__
        self.position = list(position)
        self.angle = angle
        self.speed = 10
        self.image = bullet_image
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        self.position[0] += self.speed * math.cos(math.radians(self.angle))
        self.position[1] += self.speed * math.sin(math.radians(self.angle))
        self.rect.center = self.position

    #def draw(self, screen):
    #    screen.blit(self.image, self.rect.topleft)

    def draw(self, screen):
        # Поворот зображення снаряду
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        new_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, new_rect.topleft)

# Основна функція гри
def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = [Enemy() for _ in range(10)]
    bullets = []

    running = True
    while running:
        screen.fill(BLACK)

        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Стріляти
                    bullets.append(Bullet(player.position, player.angle))
                    player.apply_recoil()  # Застосувати віддачу

        # Рух гравця
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move("forward")
        if keys[pygame.K_DOWN]:
            player.move("backward")
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")

        # Оновлення куль
        for bullet in bullets[:]:  # Ітеруємо по копії списку, щоб безпечно видаляти елементи
            bullet.update()

        # Перевірка зіткнень куль з ворогами
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if math.hypot(bullet.position[0] - enemy.position[0], bullet.position[1] - enemy.position[1]) < 20:
                    enemy.health -= 10
                    bullets.remove(bullet)
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                    break

        # Оновлення віддачі
        player.update_recoil()

        # Малювання об'єктів
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)

        # Оновлення екрана
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

""" Що змінено:
1. Завантаження зображень:
   - Використовується функція `load_image`, яка завантажує зображення з папки `images`.
   - Зображення для гравця, ворогів і куль завантажуються у відповідні класи.

2. Відображення зображень:
   - Замість простих геометричних фігур використовуються зображення.
   - Гравець може обертатися, і його зображення повертається відповідно до кута.

3. Розташування зображень:
   - Кожен об'єкт має `rect`, який визначає його позицію на екрані.

### Як підготувати зображення:
1. Створіть папку `images` у тому ж каталозі, де знаходиться ваш код.
2. Додайте туди зображення:
   - `player.png` — зображення гравця.
   - `enemy.png` — зображення ворога.
   - `bullet.png` — зображення кулі.

### Приклад зображень:
- `player.png`: Маленький танк або персонаж.
- `enemy.png`: Червоний танк або ворог.
- `bullet.png`: Невелика кулька або снаряд.

### Як запустити:
1. Встановіть Pygame: `pip install pygame`.
2. Запустіть код.
3. Використовуйте клавіші `W`, `A`, `S`, `D` для руху, пробіл для стрільби.
"""