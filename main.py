import numpy as np
import time
import msvcrt
from src.conway.logic import apply_rules
from src.conway.renderer import render_grid
from src.conway.patterns import get_random, get_fountain, get_snake, get_mutate


def run_simulation(grid: np.ndarray, base_delay: float = 0.2):
    grid = grid.copy()
    step_count = 0
    current_delay = base_delay

    while True:
        # Calculate current state stats
        pop = int(np.sum(grid))
        dens = pop / grid.size

        # Calculate births and deaths for visual feedback
        new_grid = apply_rules(grid)
        births = (grid == 0) & (new_grid == 1)
        deaths = (grid == 1) & (new_grid == 0)

        # Prepare stats for the renderer
        stats = {
            "pop": pop,
            "dens": dens,
            "step": step_count,
            "speed": 1.0 / current_delay,
        }

        # Render the current grid with birth/death markers
        render_grid(grid, births, deaths, stats)

        # Advance the grid for the next step
        grid = new_grid
        step_count += 1

        # Variable Speed: more life -> faster, less life -> slower
        # Range: 0.1s (fast) to 1.0s (slow)
        current_delay = base_delay * (2.0 - dens)
        current_delay = max(0.1, min(1.0, current_delay))

        # Check for key press (non-blocking)
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8", errors="ignore").lower()
            print(f"\n[Input: {key}]")
            if key == "r":
                grid = get_random()
                print("¡Cambio a Random!")
            elif key == "f":
                grid = get_fountain()
                print("¡Cambio a Fountain!")
            elif key == "s":
                grid = get_snake()
                print("¡Cambio a Snake!")
            elif key == "m":
                grid = get_mutate(grid)
                print("¡Mutación aplicada!")
            elif key == "q":
                print("Saliendo...")
                break
            else:
                print(f"Tecla '{key}' no reconocida.")
            time.sleep(0.5)

        time.sleep(current_delay)


if __name__ == "__main__":
    try:
        run_simulation(np.zeros((20, 20)))
    except KeyboardInterrupt:
        print("\nSimulación terminada.")
    except Exception as e:
        print(f"\nError: {e}")
