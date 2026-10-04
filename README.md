# Gridworld starter — S0

Build a small Python grid-world in a group of eight students. This is the
starting point for S0: methods raising `NotImplementedError` are your exercises.
The supplied Pygame preview works immediately; the game becomes playable after
S0-02 through S0-05 are implemented.

## Fork and prepare your group repository

1. Use **Fork** on GitHub to create the repository your group will work in.
2. Give your teammates access to that group repository, then each student clones it.
3. If the fork has no Issues tab, enable **Issues** in its repository Settings.
   Use **Issues → New issue** to create each of the five supplied S0 issue templates.
4. Create branches and open PRs against **your group's fork**, with its `main`
   branch as the base. Check the base repository: GitHub may suggest the upstream
   starter instead. Keep the group's work and reviews in its own repository.

Replace `YOUR-GROUP` and `YOUR-REPO` with the owner and name of the group fork:

```sh
git clone https://github.com/YOUR-GROUP/YOUR-REPO.git
cd YOUR-REPO
```

The project files are directly in this directory; there is no `project/` subfolder.
Each student then follows S0-01 to install the tools and add their own name.
The Contributors section starts empty.

The [S0 interfaces and rules](docs/s0.md) and
[five issue templates](.github/ISSUE_TEMPLATE/) are included in every fork.
Create the issues in the group repository from those templates; do not rely on
issue numbers from the original course repository.
See GitHub's [forking guide](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo)
for the GitHub steps.

## Install

Use Python 3.12 and [uv](https://docs.astral.sh/uv/getting-started/installation/).
Run these commands from this directory:

```sh
uv sync --locked
uv run python -m gridworld.views.pygame_render
```

The preview opens a window showing the map without a game engine. Escape or the
window close button exits. Sprites are embedded in the supplied file; no asset
downloads are needed.

## Five issues

Organize implementation tasks and peer reviews yourselves.

- **S0-01 — Set up the repository and development environment.** Every student
  installs the project, opens the preview and submits their own PR adding their
  name to the Contributors section below. Review and merge all eight PRs, then
  update every local checkout from `main`.
- **S0-02 — Implement Tile, Level and Player.** Work in `gridworld/models/`.
- **S0-03 — Implement Engine and the game rules.** Work in `gridworld/engine.py`.
- **S0-04 — Implement input and terminal rendering.** Work in
  `gridworld/controllers/controller.py`, `gridworld/controllers/terminal_input.py`
  and `gridworld/views/bash_render.py`.
- **S0-05 — Create the application launcher with a renderer argument.** Complete
  `gridworld/__main__.py` to select and connect the terminal or Pygame components.

Keep the supplied public signatures. Review `gridworld/contracts.py` with the tutor.
Preserve `levels/n0.json` and the supplied `BashRender.refresh` implementation.

**`gridworld/views/pygame_render.py` and `gridworld/controllers/pygame_input.py`
are fully supplied. You do not need to open or modify them.**

## Game state

`Engine.get_state()` returns an independent dictionary matching `initial_state.json`.
Its eight fields are `level`, `entities`, `player_id`, `status`,
`turn`, `message`, `interaction` and `extras`. In the base game, `interaction` is
`None` and `extras` is empty. Each snapshot, including nested lists, is independent
of the model.

`Player.to_state()` returns `id="player-1"`, `kind="player"`, `x`, `y` and
`appearance="player"`. The player is the only entity in S0 and is drawn last.
The terminal displays `.` for floor, `#` for walls, `E` for the exit, `P` for the
player and `?` for an unknown appearance. Display the turn as `Turn: N` and the
victory message exactly as `Victory!`.

## Connect the supplied view

In S0-05, load the selected `Level`, then connect the components. For graphical
mode, use the following wiring with your loaded `level`:

```python
from gridworld.engine import Engine
from gridworld.controllers.controller import Controller
from gridworld.controllers.pygame_input import PygameInput
from gridworld.controllers.terminal_input import TerminalInput
from gridworld.views.bash_render import BashRender
from gridworld.views.pygame_render import PygameRender

renderer = PygameRender()
input_source = PygameInput(renderer)
controller = Controller(input_source=input_source)
engine = Engine(level, controller, renderer)
renderer.start()
try:
    engine.run()
finally:
    renderer.close()
```

For terminal mode, use `BashRender()` and `Controller(input_source=TerminalInput())`.
Pygame input does not block waiting for a key. If it returns `None`, do not advance
the game, but keep polling. All Pygame calls stay on the main thread. After victory,
keep reading until the user quits.

After completing the exercises, both commands must work:

```sh
uv run python -m gridworld --render terminal
uv run python -m gridworld --render pygame
```

Terminal is the default when `--render` is omitted. `--level` selects the JSON map
and defaults to `levels/n0.json`. `--help` lists the arguments. The launcher remains
unfinished in the starter; only the standalone preview works before implementation.

The terminal accepts ZQSD followed by Enter, space to wait, and `:quit` to exit.
Pygame also accepts arrow keys; Escape or the window close button exits.

## Manual acceptance at the start of S1

- Start at `(1, 1)`, with the exit at `(5, 1)`, turn `0` and status `playing`.
- Attempt `west`: stay at `(1, 1)` and advance to turn `1`. An unknown key changes nothing.
- In a fresh game, play `east, south, south, east, east, east, north, north`:
  reach `(5, 1)` at turn `8`, with status `won` and message `Victory!`.
- After victory, movement and waiting do not change the state; quitting still works.
- Demonstrate identical results and clean shutdown in both renderers.
- Present the eight onboarding PRs and the reviewed implementation PRs; explain your code.

S0 uses manual checks. Automated unit tests begin in S1. Score, timer and reset are optional.

## Protocols and implementations

`gridworld/contracts.py` supplies the declarations:

- `Renderer`: `start()`, `update_render(json_state)`, `close()`.
- `InputSource`: `read_key() -> str | None`.
- `Action`: `north`, `east`, `south`, `west`, `wait`, `quit`.

Concrete classes implement these contracts. BashRender and PygameRender follow
Renderer; TerminalInput and PygameInput follow InputSource. Explicit inheritance
from a Protocol is not required. Controller translates keys into actions; Engine
applies the rules. Protocols do not contain those implementations.

## Contributors

<!-- Each student adds their own name here in a separate PR for S0-01. -->

## Credits

Sprites: [Kenney Tiny Dungeon](https://kenney.nl/assets/tiny-dungeon), CC0.
