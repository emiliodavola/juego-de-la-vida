import os
import numpy as np
import colorama
from colorama import Fore, Style

colorama.init()


def render_grid(grid: np.ndarray, births: np.ndarray, deaths: np.ndarray, stats: dict):
    """
    Renders a 2D numpy array with birth, death, and status bar.
    """
    os.system("cls" if os.name == "nt" else "clear")
    rows, cols = grid.shape

    # Status Bar
    header_len = cols * 2
    print(Fore.CYAN + "=" * header_len + Style.RESET_ALL)
    print(
        f" [Pop: {stats['pop']} | Dens: {stats['dens']:.1%}] "
        + Fore.CYAN
        + "=" * (header_len - 28)
        + Style.RESET_ALL
    )
    print(Fore.CYAN + "-" * header_len + Style.RESET_ALL)

    output = []
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if births[r, c] == 1:
                row_str += Fore.YELLOW + "● " + Style.RESET_ALL
            elif grid[r, c] == 1:
                row_str += Fore.GREEN + "* " + Style.RESET_ALL
            elif deaths[r, c] == 1:
                row_str += Fore.RED + "· " + Style.RESET_ALL
            else:
                row_str += "  "
        output.append(row_str)

    print("\n".join(output))
    print(Fore.CYAN + "-" * header_len + Style.RESET_ALL)
    print(
        f" [Step: {stats['step']} | Speed: {stats['speed']:.1f}x] "
        + Fore.CYAN
        + "=" * (header_len - 28)
        + Style.RESET_ALL
    )
    print(Fore.CYAN + "=" * header_len + Style.RESET_ALL)
    print("\n[f: Fountain | s: Snake | m: Mutation | r: Random | q: Salir]")
    print(Style.RESET_ALL)
