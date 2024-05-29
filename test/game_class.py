class AngryBirdsGame:
    def __init__(self):
        pygame.init()
        # 创建游戏的窗口 658 * 370 根据要显示图片的大小设置
        self.screen = pygame.display.set_mode((658, 370), 0, 32)
        init_all_sprite_info()
        # 初始化 pymunk
        self.space = pm.Space()
        self.space.gravity = (0.0, -700.0)
        self.welcome = Welcome(self.space, self.screen)
        self.choice_level = ChoiceLevel(self.space, self.screen)
        self.status = "welcome"

    def run(self):
        # 获取游戏时钟
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                mouse_up = False
                mouse_pos = pygame.mouse.get_pos()
                # 关闭事件，进行退出处理
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.status == "choice":
                        no = self.choice_level.choice(*mouse_pos)
                        print("mouse_button_left_down :" + str(no))
                    mouse_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    print("mouse_button_left_up")
                    mouse_pressed = False
                    mouse_up = True

            if self.status == "welcome":
                self.welcome.run()
                if self.welcome.status == 'end':
                    self.status = "choice"

            if self.status == "choice":
                self.choice_level.run()
                if self.choice_level.status == 'end':
                    level = self.choice_level.level_no
                    self.status = "level"
                    self.current_level = Level("level1", "./resources/level/level-" + str(level) + ".tmx", self.space,
                                               self.screen)
            if self.status == "level":
                self.current_level.handle_sling(mouse_pos, mouse_pressed, mouse_up)
                self.current_level.run()
                if self.current_level.status == "choice":
                    self.status = "choice"
                elif self.current_level.status == "next":
                    level = self.self.current_level.level_no + 1
                    self.current_level = Level("level1", "./resources/level/level_" + str(level) + ".tmx", self.space,
                                               self.screen)
                elif self.current_level.status == "again":
                    level = self.self.current_level.level_no
                    self.current_level = Level("level1", "./resources/level/level_" + str(level) + ".tmx", self.space,
                                               self.screen)
                elif self.current_level.status == "exit":
                    self.status = "exit"
            if self.status == "exit":
                break

            # 通过时钟对象指定循环频率
            clock.tick(50)
            # 调用flip方法更新显示,也可以使用update方法
            pygame.display.flip()

            dt = 1.0 / 50.0
            self.space.step(dt)
