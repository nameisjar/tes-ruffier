from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze Game')
back = (0, 0, 0)
window.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
                
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)

    def fire(self):
        bullet = Bullet('bullet.png', 10, 15, self.rect.right, self.rect.centery, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    direction = "kiri"
    def __init__(self, picture, w, h, x, y, speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.speed = speed
    
    def update(self):
        if self.rect.x <= 470:
            self.direction = "kanan"
        if self.rect.x >= win_width - 85:
            self.direction = "kiri"
        if self.direction == "kiri":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        # menghilang setelah mencapai tepi layar
        if self.rect.x > win_width+10:
            self.kill()

wall_1 = GameSprite('platform2_v.png', 60, 300, win_width // 2 - 30, win_height // 2 - 150)
wall_2 = GameSprite('platform2.png', 225, 60, win_width // 2 - 250, win_height // 2 - 30)
barriers = sprite.Group()
barriers.add(wall_1)
barriers.add(wall_2)
bullets = sprite.Group()
enemy_1 = Enemy('cyborg.png', 60, 60, 600, 140, 2)
enemy_2 = Enemy('cyborg.png', 60, 60, 600, 200, 2)
monsters = sprite.Group()
monsters.add(enemy_1)
monsters.add(enemy_2)
final = GameSprite('pac-1.png', 60, 60, win_width - 100, win_height - 100)
hero = Player('hero.png', 60, 60, 100, 100, 0, 0)

finish = False
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                hero.y_speed = -5
            elif e.key == K_DOWN:
                hero.y_speed = 5
            elif e.key == K_RIGHT:
                hero.x_speed = 5
            elif e.key == K_LEFT:
                hero.x_speed = -5
            elif e.key == K_SPACE:
                hero.fire()
        elif e.type == KEYUP:
            if e.key == K_UP:
                hero.y_speed = 0
            elif e.key == K_DOWN:
                hero.y_speed = 0
            elif e.key == K_RIGHT:
                hero.x_speed = 0
            elif e.key == K_LEFT:
                hero.x_speed = 0

    if finish != True:
        window.fill(back)
        hero.reset()
        hero.update()
        barriers.draw(window)
        bullets.draw(window)
        bullets.update()
        monsters.draw(window)
        monsters.update()
        final.reset()
        sprite.groupcollide(bullets, barriers, True, False)
        sprite.groupcollide(bullets, monsters, False, True)
        if sprite.collide_rect(hero, final):
            winner = transform.scale(image.load('thumb.jpg'), (win_width, win_height))
            window.blit(winner, (0, 0))
            finish = True
        if sprite.spritecollide(hero, monsters, False):
            winner = transform.scale(image.load('game-over_1.png'), (win_width, win_height))
            window.blit(winner, (0, 0))
            finish = True
    display.update()