# Gridworld starter

A small Python grid-world project built during class. The code contains skeletons
to complete and a supplied Pygame preview that works from the start.

## Get started

Fork this repository for your group, then clone your fork:

```sh
git clone https://github.com/YOUR-GROUP/YOUR-REPO.git
cd YOUR-REPO
```

Use Python 3.12 and [uv](https://docs.astral.sh/uv/getting-started/installation/).
Install the dependencies and open the preview:

```sh
uv sync --locked
uv run python -m gridworld.views.pygame_render
```

The preview displays a fixed map. Close it with Escape or the window close
button. The playable game is not implemented yet; unfinished methods raise
`NotImplementedError`.

When opening a pull request, select your group's fork as the base repository.

## Repository tour

| Path | What you will find |
| --- | --- |
| [`gridworld/models/`](gridworld/models/) | Skeletons for tiles, the level and the player. |
| [`gridworld/engine.py`](gridworld/engine.py) | Skeleton for game rules and the game loop. |
| [`gridworld/controllers/`](gridworld/controllers/) | Keyboard input sources and the controller that translates keys into actions. |
| [`gridworld/views/`](gridworld/views/) | Terminal rendering skeleton and supplied Pygame view. |
| [`gridworld/contracts.py`](gridworld/contracts.py) | Shared data formats and interfaces between components. |
| [`gridworld/__main__.py`](gridworld/__main__.py) | Command-line entry point, with rendering and level arguments already declared. |
| [`levels/n0.json`](levels/n0.json) | The starting map: terrain, player start and exit coordinates. |
| [`initial_state.json`](initial_state.json) | Example of the game state passed to a view. |
| [`pyproject.toml`](pyproject.toml), [`uv.lock`](uv.lock), [`.python-version`](.python-version) | Dependencies and Python version used by the project. |

The engine applies game rules, the controller translates input, and the views
show the resulting state.

`PygameRender`, `PygameInput` and `BashRender.refresh` are supplied. The Pygame
sprites are embedded, so no separate asset download is needed.

## Continue with S2

Keep your group's completed S0 game and S1 tests. S2 adds your own Python HTTP
adapter, dialogue data, LLM service and integration. The supplied renderer includes
the 2D/3D views and the sphinx dialogue; no browser code is required from you.

Start with the [S2 project guide](https://davidbert.github.io/OutilsNumeriques/s2/).
It provides the renderer and four starter downloads, launch commands, shared
contracts and [Ollama setup](https://davidbert.github.io/OutilsNumeriques/s2/llm/).
Read each archive's README and merge the files into your existing project.
Do not replace your completed engine or existing tests with blank skeletons.

The assignments are public and bilingual, with French before English:

- [S2-01 — Python HTTP adapter](https://github.com/DavidBert/INSA-project-gridworld-starter/issues/1)
- [S2-02 — Dialogue contract and map](https://github.com/DavidBert/INSA-project-gridworld-starter/issues/2)
- [S2-03 — LLM service and deterministic fake](https://github.com/DavidBert/INSA-project-gridworld-starter/issues/3)
- [S2-04 — Sphinx integration](https://github.com/DavidBert/INSA-project-gridworld-starter/issues/4)

Use these as templates for issues in your group's fork. Implement and review your
PRs in that fork. You can begin the API, contract and service independently; bring
their outputs together before testing the full integration. A real model is needed
only for the final service evaluation and demonstration, not automated tests.

## Contributors

## Credits

Sprites: [Kenney Tiny Dungeon](https://kenney.nl/assets/tiny-dungeon), CC0.
