import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simulação de Fazenda")
clock = pygame.time.Clock()
running = True

def draw_scenario(screen):
    # Campos de cultivo
    pygame.draw.rect(screen, (34, 139, 34), (50, 100, 200, 150))
    pygame.draw.rect(screen, (34, 139, 34), (300, 100, 200, 150))

    # Estábulo
    pygame.draw.rect(screen, (139, 69, 19), (550, 100, 200, 150))

    # Lago
    pygame.draw.ellipse(screen, (0, 0, 255), (50, 300, 150, 100))

    # Celeiro
    pygame.draw.rect(screen, (255, 0, 0), (300, 300, 200, 150))
    pygame.draw.rect(screen, (255, 255, 255), (375, 350, 50, 100))

    # Casa do fazendeiro
    pygame.draw.rect(screen, (255, 255, 0), (550, 300, 150, 100))
    pygame.draw.rect(screen, (255, 255, 255), (600, 350, 50, 50))

class Farm:
    def __init__(self):
        self.fields = [(50, 100, 200, 150), (300, 100, 200, 150)]
        self.animals = [(550, 100, 200, 150)]
        self.lake = (50, 300, 150, 100)
        self.barn = (300, 300, 200, 150)
        self.house = (550, 300, 150, 100)

    def draw(self, screen):
        # Desenhe campos
        for field in self.fields:
            pygame.draw.rect(screen, (34, 139, 34), field)

        # Desenhe estábulo
        for stable in self.animals:
            pygame.draw.rect(screen, (139, 69, 19), stable)

        # Desenhe lago
        pygame.draw.ellipse(screen, (0, 0, 255), self.lake)

        # Desenhe celeiro
        pygame.draw.rect(screen, (255, 0, 0), self.barn)
        pygame.draw.rect(screen, (255, 255, 255), (375, 350, 50, 100))

        # Desenhe casa do fazendeiro
        pygame.draw.rect(screen, (255, 255, 0), self.house)
        pygame.draw.rect(screen, (255, 255, 255), (600, 350, 50, 50))

    def handle_click(self, pos):
        x, y = pos
        for field in self.fields:
            if field[0] < x < field[0] + field[2] and field[1] < y < field[1] + field[3]:
                print("Você clicou em um campo de cultivo!")

farm = Farm()

# Adicione a lógica de interatividade no loop principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            farm.handle_click(event.pos)

    screen.fill((135, 206, 235))  # Cor de fundo (céu)
    farm.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()