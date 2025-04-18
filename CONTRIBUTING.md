# Contributing

All contributions are welcome! Besides code contributions, this includes things like documentation improvements, bug reports, and feature requests.

You should first check if there is a [GitHub issue](https://github.com/joshuadavidthomas/llm-uv-tool/issues) already open or related to what you would like to contribute. If there is, please comment on that issue to let others know you are working on it. If there is not, please open a new issue to discuss your contribution.

Not all contributions need to start with an issue, such as typo fixes in documentation or version bumps to Python or Django that require no internal code changes, but generally, it is a good idea to open an issue first.

We adhere to Django's Code of Conduct in all interactions and expect all contributors to do the same. Please read the [Code of Conduct](https://www.djangoproject.com/conduct/) before contributing.

## Requirements

- [uv](https://github.com/astral-sh/uv) - Modern Python toolchain that handles:
  - Python version management and installation
  - Virtual environment creation and management
  - Fast, reliable dependency resolution and installation
  - Reproducible builds via lockfile
- [direnv](https://github.com/direnv/direnv) (Optional) - Automatic environment variable loading
- [just](https://github.com/casey/just) (Optional) - Command runner for development tasks

### `Justfile`

The repository includes a `Justfile` that provides all common development tasks with a consistent interface. Running `just` without arguments shows all available commands and their descriptions.

<!-- [[[cog
import subprocess
import cog

output_raw = subprocess.run(["just", "--list", "--list-submodules"], stdout=subprocess.PIPE)
output_list = output_raw.stdout.decode("utf-8").split("\n")

cog.outl("""\
```bash
$ just
$ # just --list --list-submodules
""")

for i, line in enumerate(output_list):
    if not line:
        continue
    cog.out(line)
    if i < len(output_list):
        cog.out("\n")

cog.out("```")
]]] -->
<!-- [[[end]]] -->

All commands below will contain the full command as well as its `just` counterpart.

## Setup

The following instructions will use `uv` and assume a Unix-like operating system (Linux or macOS).

Windows users will need to adjust commands accordingly, though the core workflow remains the same.

Alternatively, any Python package manager that supports installing from `pyproject.toml` ([PEP 621](https://peps.python.org/pep-0621/)) can be used. If not using `uv`, ensure you have Python installed from [python.org](https://www.python.org/) or another source such as [`pyenv`](https://github.com/pyenv/pyenv).

1. Fork the repository and clone it locally.

2. Use `uv` to bootstrap your development environment.

   ```bash
   uv python install
   uv sync --locked
   # just bootstrap
   ```

   This will install the correct Python version, create and configure a virtual environment, and install all dependencies.

## Linting and Formatting

This project enforces code quality standards using [`pre-commit`](https://github.com/pre-commit/pre-commit).

To run all formatters and linters:

```bash
uv run --with pre-commit-uv pre-commit run --all-files
# just lint
```

The following checks are run:

- [ruff](https://github.com/astral-sh/ruff) - Fast Python linter and formatter
- Code formatting for Python files in documentation ([blacken-docs](https://github.com/adamchainz/blacken-docs))
- TOML and YAML validation
- Basic file hygiene (trailing whitespace, file endings)

To enable pre-commit hooks after cloning:

```bash
uv run --with pre-commit-uv pre-commit install
```

Configuration for these tools can be found in:

- [`.pre-commit-config.yaml`](.pre-commit-config.yaml) - Pre-commit hook configuration
- [`pyproject.toml`](pyproject.toml) - Ruff and other tool settings

## Continuous Integration

This project uses GitHub Actions for CI/CD. The workflows can be found in [`.github/workflows/`](.github/workflows/).

- [`release.yml`](.github/workflows/release.yml) - Runs on GitHub release creation
  - Runs the [`test.yml`](.github/workflows/test.yml) workflow
  - Builds package
  - Publishes to PyPI

PRs must pass all CI checks before being merged.
