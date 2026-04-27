import random
import pygame

# Constante pentru dimensiunile ferestrei și ale grilei
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
UPDATE_INTERVAL_MS = 5000  # ms

def generate_random_colors():
    """
    Generează o matrice de culori RGB aleatoare pentru grilă.
    Returnează o listă de liste (matrice 10x10), unde fiecare element 
    este un tuplu (R, G, B).
    """
    return [
        [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]

def main():
    pygame.init()

    # Setarea ferestrei și a titlului
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (Auto la 5s sau SPACE)")

    # Generarea inițială a grilei de culori
    color_grid = generate_random_colors()

    # Stocăm timpul (în milisecunde) la care a avut loc ultima generare
    last_update_time = pygame.time.get_ticks()

    # Bucla principală a jocului
    is_running = True
    while is_running:
        current_time = pygame.time.get_ticks()

        # Verificăm dacă au trecut 5 secunde (5000 ms) de la ultima actualizare
        if current_time - last_update_time >= UPDATE_INTERVAL_MS:
            color_grid = generate_random_colors()
            last_update_time = current_time

        # Gestionarea evenimentelor de la tastatură/mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Permitem și regenerarea manuală la apăsarea tastei SPACE
                    color_grid = generate_random_colors()
                    # Resetăm timer-ul pentru a nu se schimba din nou prea curând
                    last_update_time = pygame.time.get_ticks()

        # Curățarea ecranului cu fundal negru
        screen.fill((0, 0, 0))

        # Desenarea grilei de culori pe ecran
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                # Extragem culoarea din matrice pentru celula curentă
                cell_color = color_grid[row][col]
                
                # Calculăm coordonatele X și Y pe ecran
                rect_x = col * CELL_SIZE
                rect_y = row * CELL_SIZE
                
                # Desenăm dreptunghiul corespunzător
                pygame.draw.rect(screen, cell_color, (rect_x, rect_y, CELL_SIZE, CELL_SIZE))

        # Actualizarea vizuală a ferestrei
        pygame.display.flip()

    # Închiderea corectă a aplicației
    pygame.quit()

# Punctul de intrare în program
if __name__ == "__main__":
    main()