# Copilot instructions

## Project layout and commands

- This repository contains independent `uv` projects under `viikko1/`,
  `viikko2/`, and `viikko3/`. Run commands from the relevant project directory
  using `uv run ...`; there is no root-level runner.
- Install/sync a project with `uv sync`.
- Week 1 unit tests:

  ```bash
  cd viikko1/nhl-statistics && uv run pytest
  uv run pytest src/tests/statistics_service_test.py::TestStatisticsService::test_team_returns_players_of_team

  cd ../riippuvuuksien-injektointi && uv run pytest
  uv run pytest src/tests/laskin_test.py::TestLaskin::test_yksi_summa_oikein
  ```

- `viikko2/nhl-reader`: run with `uv run python src/index.py`. The week 2
  projects currently have no repository-local tests or lint command.
- `viikko3/hello-robot`: `uv run robot src/tests`; one test:
  `uv run robot --test "Increase Counter Once" src/tests/increase_counter.robot`.
- `viikko3/login`: start the app with `uv run python src/index.py`. It listens
  on port 5001 (`http://localhost:5001`). In another terminal, with the server
  still running, execute `uv run robot src/tests`; use
  `uv run robot --variable HEADLESS:true src/tests` in headless environments.
  A single test can be run with:
  `uv run robot --variable HEADLESS:true --test "Login With Correct Credentials" src/tests/login.robot`.
- Python unit tests are executed with `uv run pytest`.
- No lint configuration or build command is defined.

## Architecture and conventions

- Each project uses a `src/` layout with simple flat imports; preserve the
  existing project working-directory assumptions.
- Week 1 code separates domain/services from I/O and uses injected stubs in
  unit tests.
- `viikko2/nhl-reader` separates HTTP/JSON retrieval (`PlayerReader`), data
  (`Player`), and filtering/sorting (`PlayerStats`).
- `viikko3/hello-robot` exposes the in-memory `Counter` through
  `CounterLibrary.py`; its Robot tests do not need a server.
- `viikko3/login` is Flask in `src/app.py`, started by `src/index.py`.
  Templates are in `src/templates`; routes delegate business rules to the
  singleton `user_service`, which uses the in-memory singleton
  `user_repository`.
- Username/password validation and authentication belong in
  `src/services/user_service.py`: `UserService.validate` handles registration
  rules and `UserService.check_credentials` handles login checks. Keep Flask
  routes focused on form handling, redirects, and flashed errors.
- Login Robot suites use `src/tests/resource.robot` and `AppLibrary.py`.
  Tests reset state through `POST /tests/reset`; preserve this setup path and
  keep browser scenarios deterministic.
- Do not change `viikko4/tdd-ostoskori/src/ostos.py` or
  `viikko4/tdd-ostoskori/src/tuote.py`.
- Do not edit tests unless the user explicitly asks for test changes.
- Implement only the absolutely minimal code required for the current tests
  to pass.
