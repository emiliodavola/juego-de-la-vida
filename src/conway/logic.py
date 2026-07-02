import numpy as np


def apply_rules(grid: np.ndarray) -> np.ndarray:
    """
    Applies Conway's Game of Life rules to a 2D numpy array.
    """
    # Count neighbors for each cell
    # Using a simple 3x3 kernel convolution-like approach
    # For simplicity, we use manual slicing
    rows, cols = grid.shape
    new_grid = np.zeros_like(grid)

    # Pad to handle edges (assume boundary cells stay dead)
    padded = np.pad(grid, 1, mode="constant", constant_values=0)

    # Neighbors count
    # Sum of 3x3 area minus the cell itself
    neighbors = (
        padded[0:-2, 0:-2]
        + padded[0:-2, 1:-1]
        + padded[0:-2, 2:]
        + padded[1:-1, 0:-2]
        + padded[1:-1, 2:]
        + padded[2:, 0:-2]
        + padded[2:, 1:-1]
        + padded[2:, 2:]
    ) - padded[1:-1, 1:-1]

    # Apply rules
    # 2 or 3 neighbors -> survives
    # 3 neighbors (dead) -> becomes alive
    survive = (grid == 1) & ((neighbors == 2) | (neighbors == 3))
    birth = (grid == 0) & (neighbors == 3)

    new_grid[survive | birth] = 1
    return new_grid
