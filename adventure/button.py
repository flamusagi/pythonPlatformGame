import pygame

#创建按钮类
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self,screen):
        action = False
        # 得到鼠标的位置
        pos = pygame.mouse.get_pos()
        # 检测鼠标是否经过按钮位置和是否已点击
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # 将按钮画到屏幕上
        screen.blit(self.image, self.rect)

        return action
