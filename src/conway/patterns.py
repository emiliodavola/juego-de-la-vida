import numpy as np


def get_random():
    """Returns a random grid."""
    size = 20
    grid = np.random.choice([0, 1], size=(size, size), p=[0.8, 0.2])
    return grid


def get_fountain():
    """Returns a Fountain pattern (expanding center)."""
    size = 20
    grid = np.zeros((size, size), dtype=int)
    grid[10, 10] = 1
    grid[9, 10] = 1
    grid[11, 10] = 1
    grid[10, 9] = 1
    grid[10, 11] = 1
    return grid


def get_snake():
    """Returns a Snake pattern (linear sequence)."""
    size = 20
    grid = np.zeros((size, size), dtype=int)
    for i in range(5):
        grid[5 + i, 5 + i] = 1
    return grid


def get_mutate(grid: np.ndarray):
    """Mutates the current grid by adding random noise."""
    new_grid = grid.copy()
    noise_mask = np.random.choice([0, 1], size=grid.shape, p=[0.95, 0.05])
    new_grid = np.logical_xor(new_grid, noise_mask).astype(int)
    return new_grid
