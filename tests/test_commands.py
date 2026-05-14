from __future__ import annotations

import click
from click.testing import CliRunner

import llm_uv_tool


def cli():
    group = click.Group()
    llm_uv_tool.register_commands(group)
    return group


def test_install_preserves_current_llm_version(monkeypatch, tmp_path):
    calls = []

    monkeypatch.setattr(llm_uv_tool, "user_dir", lambda: tmp_path)
    monkeypatch.setattr(llm_uv_tool, "get_plugins", lambda: [])
    monkeypatch.setattr(llm_uv_tool, "version", lambda package: "0.32a2")
    monkeypatch.setattr(
        llm_uv_tool.subprocess,
        "run",
        lambda args, check: calls.append((args, check)),
    )

    result = CliRunner().invoke(cli(), ["install", "llm-llama-cpp"])

    assert result.exit_code == 0
    assert calls == [
        (
            [
                "uv",
                "tool",
                "install",
                "--force",
                "llm==0.32a2",
                "--with",
                "llm-llama-cpp",
            ],
            True,
        )
    ]


def test_uninstall_preserves_current_llm_version(monkeypatch, tmp_path):
    calls = []

    monkeypatch.setattr(llm_uv_tool, "user_dir", lambda: tmp_path)
    monkeypatch.setattr(llm_uv_tool, "get_plugins", lambda: [{"name": "llm-llama-cpp"}])
    monkeypatch.setattr(llm_uv_tool, "version", lambda package: "0.32a2")
    monkeypatch.setattr(
        llm_uv_tool.subprocess,
        "run",
        lambda args, check: calls.append((args, check)),
    )

    result = CliRunner().invoke(cli(), ["uninstall", "-y", "llm-llama-cpp"])

    assert result.exit_code == 0
    assert calls == [
        (
            ["uv", "tool", "install", "--force", "llm==0.32a2"],
            True,
        )
    ]
