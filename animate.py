
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
import pygame
import glob
 
SIZE = WIDTH, HEIGHT = 600, 600 #the width and height of our screen
FPS = 20 #Frames per second
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super(MySprite, self).__init__()
        im = glob.glob(f"png\\{action}*.png")
        lenim = len(im[0])
        self.images = [pygame.image.load(img) for img in glob.glob(f"png\\{action}*.png") if len(img) == lenim]
        self.images2 = [pygame.image.load(img) for img in glob.glob(f"png\\{action}*.png") if len(img) &gt; lenim]
        self.images.extend(self.images2)
        self.index = 0
        self.rect = pygame.Rect(5, 5, 150, 198)
 
    def update(self):
        if self.index &gt;= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1
 
def action(action):
    my_sprite = MySprite(action)
    my_group = pygame.sprite.Group(my_sprite)
    return my_group
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Press i w r j d or arrows and space")
    my_sprite = MySprite("idle")
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_LEFT:
                    my_group = action("walk")
                if event.key == pygame.K_d:
                    my_group = action("dead")                
                if event.key == pygame.K_j or event.key == pygame.K_UP:
                    my_group = action("jump")
                if event.key == pygame.K_i or event.key == pygame.K_SPACE:
                    my_group = action("idle")
                if event.key == pygame.K_r or event.key == pygame.K_RIGHT:
                    my_group = action("run")
                if event.key == pygame.K_d or event.key == pygame.K_DOWN:
                    my_group = action("dead")
 
 
        my_group.update()
        screen.fill((0,0,0))
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
 
if __name__ == '__main__':
    main()
