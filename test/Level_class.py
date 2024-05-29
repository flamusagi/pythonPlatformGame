class ChoiceLevel:
    def __init__(self, space, surface):
        self.number_group = None
        self.surface = surface
        self.space = space
        self.init_number_image()
        self.create_object()

        self.status = "start"
        self.level_no = 1

    def create_object(self):
        self.tiled_render = TiledRender("./resources/level/choice_level.tmx")
        number_group = pygame.sprite.Group()
        for layer in self.tiled_render.tmx_data.visible_layers:
            if isinstance(layer, TiledObjectGroup):
                if layer.name != "level":
                    continue
                for obj in layer:
                    number_sprite = Sprite()
                    name = obj.name
                    temp = name.split('-')
                    no = int(temp[1])
                    no -= 1
                    image = self.number_images[no]
                    scale_image = scale(image, (60, 60))
                    number_sprite.image = scale_image
                    number_sprite.rect = pygame.Rect(obj.x, obj.y, 60, 60)
                    number_sprite.no = no + 1
                    number_group.add(number_sprite)
                self.number_group = number_group
            if isinstance(layer, TiledImageLayer):
                self.background_image = pygame.image.load("./resources/images/level/" + layer.image_name).convert()

    def init_number_image(self):
        self.number_image = pygame.image.load("./resources/images/level/number.png")
        number_image_list = []
        y = 0
        for row in range(0, 4):
            x = 0
            for col in range(0, 3):
                image = self.number_image.subsurface(x, y, 179, 170)
                number_image_list.append(image)
                x += 179
            y += 170
        self.number_images = number_image_list

    def run(self):
        # 绘制图片到显示窗口
        self.surface.blit(self.background_image, (0, 0))
        self.number_group.draw(self.surface)

    def choice(self, mouse_x, mouse_y):
        for item in self.number_group:
            if item.rect.collidepoint(mouse_x, mouse_y):
                self.level_no = item.no
                self.status = "end"
                return item.no
        return None