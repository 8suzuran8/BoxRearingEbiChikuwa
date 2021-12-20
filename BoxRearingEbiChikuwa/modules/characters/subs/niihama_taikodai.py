import pygame
from modules.physical import Physical

class CharacterNiihamaTaikodai(Physical):
    def __new__(cls, image_loader, status, setting, info):
        self = super().__new__(cls, image_loader, status, setting, info)

        return self

    def initializeVariable(self, image_loader, status, setting, info):
        Physical.initializeVariable(self, image_loader, status, setting, info)

        self.animation_type_infos = [
            ['stand', 'stand'],
        ]

        animation_type_index = 0
        for animation_type_info in self.animation_type_infos:
            self.frames.append(list())
            frame_index = len(self.frames) - 1
            for i in range(self.animation_file_max[animation_type_index]):
                self.frames[frame_index].append(pygame.Surface((100, 75)).convert_alpha())

            animation_type_index += 1

        self.need_fall = False

        return

    def __init__(self, image_loader, status, setting, info):
        Physical.__init__(self, image_loader, status, setting, info)

        self.draw()

        return

    def draw(self):
        # 頭
        pygame.draw.circle(
            self.image,
            (255, 255, 255),
            (50, 20),
            20
        )

        # 体
        pygame.draw.rect(
            self.image,
            (230, 131, 32),
            (30, 20, 40, 20)
        )
        pygame.draw.rect(
            self.image,
            (230, 131, 32),
            (35, 40, 30, 10)
        )
        pygame.draw.rect(
            self.image,
            (230, 131, 32),
            (30, 50, 40, 10)
        )
        pygame.draw.line(
            self.image,
            (0, 0, 0),
            (35, 38),
            (65, 38),
            4
        )
        pygame.draw.line(
            self.image,
            (0, 0, 0),
            (30, 50),
            (70, 50),
            4
        )

        # 房
        self.makeFusa(20, 10)
        self.makeFusa(60, 10)

        # かき棒
        pygame.draw.line(
            self.image,
            (230, 131, 32),
            (0, 60),
            (100, 60),
            5
        )

        # 台場
        pygame.draw.line(
            self.image,
            (230, 131, 32),
            (40, 60),
            (40, 75),
            5
        )
        pygame.draw.line(
            self.image,
            (230, 131, 32),
            (60, 60),
            (60, 75),
            5
        )
        pygame.draw.line(
            self.image,
            (230, 131, 32),
            (40, 70),
            (60, 70),
            5
        )

        return

    def makeFusa(self, x, y, frame = 0):
        # 括り
        pygame.draw.ellipse(
            self.image,
            (0, 0, 0),
            (x + 2, y, 15, 10)
        )
        pygame.draw.ellipse(
            self.image,
            (0, 0, 0),
            (x + 2, y + 10, 15, 10)
        )
        pygame.draw.ellipse(
            self.image,
            (255, 20, 147),
            (x + 4, y + 6, 11, 8)
        )

        # 房
        #   端
        pygame.draw.line(
            self.image,
            (255, 255, 255),
            (x + 4, y + 20),
            (x + 4, y + 25),
            1
        )
        pygame.draw.line(
            self.image,
            (255, 255, 255),
            (x + 14, y + 20),
            (x + 14, y + 25),
            1
        )
        #   端の跳ね
        if frame == 0:
            pygame.draw.line(
                self.image,
                (255, 255, 255, 0),
                (x + 4, y + 25),
                (x + 2, y + 30),
                1
            )
            pygame.draw.line(
                self.image,
                (255, 255, 255, 0),
                (x + 14, y + 25),
                (x + 16, y + 30),
                1
            )
            pygame.draw.line(
                self.image,
                (255, 255, 255),
                (x + 4, y + 25),
                (x + 4, y + 30),
                1
            )
            pygame.draw.line(
                self.image,
                (255, 255, 255),
                (x + 14, y + 25),
                (x + 14, y + 30),
                1
            )
        else:
            pygame.draw.line(
                self.image,
                (255, 255, 255, 0),
                (x + 4, y + 25),
                (x + 4, y + 30),
                1
            )
            pygame.draw.line(
                self.image,
                (255, 255, 255, 0),
                (x + 14, y + 25),
                (x + 14, y + 30),
                1
            )
            pygame.draw.line(
                self.image,
                (255, 255, 255),
                (x + 4, y + 25),
                (x + 2, y + 30),
                1
            )
            pygame.draw.line(
                self.image,
                (255, 255, 255),
                (x + 14, y + 25),
                (x + 16, y + 30),
                1
            )

        #   束
        for index in range(4):
            pygame.draw.line(
                self.image,
                (255, 255, 255),
                (x + 6 + (index * 2), y + 20),
                (x + 6 + (index * 2), y + 30),
                1
            )

        return
