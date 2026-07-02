# Design Note: 01_conway_game_of_life

## Goal
Implement a terminal-based simulation of Conway's Game of Life.

## Instructions
- Use a 2D grid of cells.
- Cells are either Alive (1) or Dead (0).
- Rules:
  - A living cell with 2 or 3 living neighbors survives.
  - A dead cell with exactly 3 living neighbors becomes alive.
  - All other cases: death.
- Visualization: Use ASCII characters or terminal colors to represent the grid in real-time.
- Input: Allow starting with a random grid or a known pattern (e.g., Glider).

## Accomplished
- [ ] Workspace scaffolded.
- [ ] Design note created.

## Next Steps
- Implement the core logic in `src/conway/logic.py`.
- Implement the terminal renderer in `src/conway/renderer.py`.
- Create `main.py` to run the simulation.
