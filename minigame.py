import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60

# Установка окна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Pygame with Shooting")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Фон
background_image = pygame.Surface(window.get_size())
background_image.fill(WHITE)


# Класс игрока
class Player:
    def init(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = RED
        self.health = 100

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Ограничение передвижения в пределах окна
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


# Класс пули
class Bullet:
    def init(self, x, y):
        self.rect = pygame.Rect(x + 20, y, 10, 5)
        self.color = BLUE
        self.speed = -10  # Пули движутся вверх

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


# Используемые игровые элементы
class Enemy:
    def init(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50), 50, 50)
        self.color = GREEN

    def move(self):
        # Простое случайное движение врага
        self.rect.x += random.choice([-2, 0, 2])
        self.rect.y += random.choice([-2, 0, 2])
        # Ограничение передвижения
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


# Главная функция игры
def main():
    clock = pygame.time.Clock()
    player = Player(WIDTH // 2, HEIGHT // 2)
    bullets = []
    enemies = [Enemy() for _ in range(5)]  # Создаём 5 врагов
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Стрельба по пробелу
                    bullet = Bullet(player.rect.x, player.rect.y)
                    bullets.append(bullet)

        # Получение нажатий клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            player.move(5, 0)
        if keys[pygame.K_UP]:
            player.move(0, -5)
        if keys[pygame.K_DOWN]:
            player.move(0, 5)

        # Обновление врагов
        for enemy in enemies:
            enemy.move()

        # Обновление пуль
        for bullet in bullets[:]:
            bullet.move()
            # Удаляем пули, которые вышли за пределы экрана
            if bullet.rect.y < 0:
                bullets.remove(bullet)

            # Проверка на столкновение пули с врагом
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    enemies.remove(enemy)  # Удаляем врага
                    bullets.remove(bullet)  # Удаляем пулю
                    score += 1  # Увеличиваем счет
                    break

        # Обновление дисплея
        window.blit(background_image, (0, 0))  # Заполнение фона белым цветом
        player.draw(window)

        # Отображение врагов
        for enemy in enemies:
            enemy.draw(window)

        # Отображение пуль
        for bullet in bullets:
            bullet.draw(window)

        # Отображение здоровья и очков
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Health: {player.health}', True, BLUE)
        window.blit(score_text, (10, 10))
        score_display = font.render(f'Score: {score}', True, BLUE)
        window.blit(score_display, (10, 40))

        pygame.display.flip()
        clock.tick(FPS)  # Ограничение до 60 кадров в секунду

    pygame.quit()


if __name__ == "__main__":
    main()
"""### Изменения в коде:
1.
Класс
`Bullet`: Добавлен
класс
для
управления
пулями, который
хранит
положение, скорость
и
методы
для
их
перемещения
и
рисования.

2.
Стрельба: Игрок
может
стрелять, нажав
клавишу
"Пробел".Пули
летят
вверх
от
позиции
игрока.

3.
Проверка
столкновений: Если
пуля
сталкивается
с
врагом, враг
удаляется, а
пуля
также
удаляется.Увеличивает
счёт
при
попадании.

### Управление:
- Стрелки
для
перемещения
персонажа.
- Пробел, чтобы
стрелять.

### Примечания:
- Это
базовая
механика, и
вы
можете
улучшить
игру, добавив
больше
врагов, уровней
сложности, анимаций, звуковых
эффектов
и
улучшенного
интерфейса."""