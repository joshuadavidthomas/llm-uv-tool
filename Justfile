set dotenv-load := true
set unstable := true

[private]
default:
    @just --list

[private]
fmt:
    @just --fmt

bootstrap:
    uv python install
    uv sync --frozen

bump *ARGS:
    uv run --with bumpver bumpver {{ ARGS }}

lint:
    uv run --with pre-commit-uv pre-commit run --all-files
    just fmt

lock *ARGS:
    uv lock {{ ARGS }}
