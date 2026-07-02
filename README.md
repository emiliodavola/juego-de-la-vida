# Conway's Game of Life

This project implements an interactive, terminal-based "Observation Dashboard" for Conway's Game of Life. It features a professional retro-scientific interface with real-time status tracking, color-coded cell states, and dynamic pattern controls.

## Core Features

- **Dynamic Patterns**: The simulation can be initialized or transformed using several dynamic patterns:
  - `f`: Fountain (expanding center)
  - `s`: Snake (linear sequence)
  - `m`: Mutation (adding random noise to the current grid)
  - `r`: Random (re-randomizing the grid)
- **Real-time Dashboard**: A status bar at the top and bottom displays:
  - Population count
  - Density (%)
  - Current step number
  - Simulation speed (adjusted dynamically based on cell density)
- **Visual Feedback**: Uses terminal colors to indicate cell states:
  - Green (`*`): Alive
  - Yellow (`●`): Birth (New cell)
  - Red (`·`): Death (Cell died)
- **Interactive Controls**:
  - `f`: Fountain | `s`: Snake | `m`: Mutation | `r`: Random | `q`: Salir

## Project Structure

- `src/conway/`:
  - `logic.py`: The core implementation of Conway's rules.
  - `renderer.py`: Terminal UI management (colors and status bars).
  - `patterns.py`: Collection of dynamic and static starting patterns.
- `journal/`: Design notes and project evolution (SDD/OpenSpec).
- `main.py`: The main execution entry point for the dashboard.
- `scratch/`: Temporary development probes (e.g., dependency checks).

## Tech Stack

- `numpy`: Grid manipulation and mathematical operations.
- `colorama`: Terminal colorization for the professional UI.
- `msvcrt`: Non-blocking keyboard input (Windows).
