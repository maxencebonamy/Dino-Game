# Dino Game

A Chrome-dinosaur-style runner built with Pygame.

Jump over cacti and birds for as long as you can. The game speeds up as your score rises, tracks your high score, and lets you restart instantly after a crash.

## Table of contents

- [Dino Game](#dino-game)
	- [Table of contents](#table-of-contents)
	- [How it works](#how-it-works)
	- [Tech stack](#tech-stack)
	- [Repository structure](#repository-structure)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
	- [Running locally](#running-locally)
	- [Useful scripts](#useful-scripts)
	- [License](#license)

## How it works

1. **Start**: the dino stands idle until the player presses `Space` or `↑`, which triggers the first jump and starts the run.
2. **Move**: the ground, clouds and obstacles scroll left once the dino lands from its first jump. Ground speed increases with the score, up to a cap.
3. **Control**: `Space` / `↑` makes the dino jump, `↓` makes it duck, switching between walk and duck sprite animations.
4. **Obstacles**: cacti and birds spawn at random intervals and types ahead of the player and scroll toward the dino.
5. **Collision**: each frame, the dino's rectangle is checked against every obstacle's rectangle; a collision ends the run and shows the game-over screen.
6. **Score**: the score increases over time while running and is rendered with a sprite font; the best score of the session is kept as the high score.
7. **Restart**: pressing `Space` / `↑` on the game-over screen resets the dino, ground, clouds and score, and a new run starts.

## Tech stack

| Layer | Technologies |
| --- | --- |
| Runtime | Python, Pygame |

## Repository structure

```
.
├── assets/        Sprites for the dino, ground, clouds, obstacles, score digits and UI
├── example/        Screenshots used for documentation
├── const.py        Window size, FPS and background color
├── dino.py          Dino sprite, animation and jump physics
├── ground.py       Ground scrolling and obstacle spawning
├── cloud.py        Background cloud spawning and scrolling
├── score.py        Score counter and high score, rendered from a sprite font
├── game.py         Game state, collision detection and restart flow
├── main.py         Pygame window and main loop
├── requirements.txt Python dependencies
└── run.sh          Launches the game from the project's virtual environment
```

Each gameplay element (dino, ground, cloud, score) is its own class with `update` and `reset` methods, called from `Game`.

## Prerequisites

- [Python](https://www.python.org/) 3
- [Pygame](https://www.pygame.org/) 2.6.1

## Installation

```bash
git clone git@github.com:maxencebonamy/Dino-Game.git
cd Dino-Game
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Running locally

```bash
./run.sh
```

This runs `main.py` with the project's virtual environment. `Space` or `↑` jumps and starts the game, `↓` ducks.

## Useful scripts

| Command | Effect |
| --- | --- |
| `./run.sh` | Run the game |

## License

This project is licensed under the [MIT License](LICENSE).
