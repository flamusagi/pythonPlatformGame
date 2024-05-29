def step22_choice_level():
    """
    step22: 关卡选择
    """

    # 初始化pygame
    pygame.init()
    # 创建游戏的窗口 658 * 370 根据要显示图片的大小设置
    screen = pygame.display.set_mode((658, 370), 0, 32)
    init_all_sprite_info()
    # 初始化 pymunk
    space = pm.Space()
    space.gravity = (0.0, -700.0)
    # 获取游戏时钟
    clock = pygame.time.Clock()
    choice_level = ChoiceLevel(space, screen)

    while True:
        # 游戏循环
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
                no = choice_level.choice(*mouse_pos)
                print("mouse_button_left_down :" + str(no))
                mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("mouse_button_left_up")
                mouse_pressed = False
                mouse_up = True

        choice_level.run()
        # 通过时钟对象指定循环频率
        clock.tick(50)
        # 调用flip方法更新显示,也可以使用update方法
        pygame.display.flip()

        dt = 1.0 / 50.0
        space.step(dt)


if __name__ == '__main__':
    """
    通过main函数调用step22_choice_level
    """
    step22_choice_level()
