from __future__ import annotations

import click
from click.testing import CliRunner

import llm_uv_tool


def cli():
    group = click.Group()
    llm_uv_tool.register_commands(group)
    return group


def test_install_rebuilds_tool_with_current_prerelease_llm(monkeypatch, tmp_path):
    calls = []

    monkeypatch.setattr(llm_uv_tool, "user_dir", lambda: tmp_path)
    monkeypatch.setattr(llm_uv_tool, "version", lambda package: "0.32a2")
    monkeypatch.setattr(llm_uv_tool, "get_plugins", lambda: [])
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
    assert llm_uv_tool.get_installed_uv_tool_packages() == ["llm-llama-cpp"]


def test_install_keeps_existing_plugins_when_rebuilding(monkeypatch, tmp_path):
    calls = []
    (tmp_path / "uv-tool-packages.json").write_text('["llm-templates-github"]')

    monkeypatch.setattr(llm_uv_tool, "user_dir", lambda: tmp_path)
    monkeypatch.setattr(llm_uv_tool, "version", lambda package: "0.31")
    monkeypatch.setattr(llm_uv_tool, "get_plugins", lambda: [{"name": "llm-gemini"}])
    monkeypatch.setattr(
        llm_uv_tool.subprocess,
        "run",
        lambda args, check: calls.append((args, check)),
    )

    result = CliRunner().invoke(cli(), ["install", "--no-cache-dir", "llm-llama-cpp"])

    assert result.exit_code == 0
    args, check = calls[0]
    assert check is True
    assert args[:6] == [
        "uv",
        "tool",
        "install",
        "--force",
        "llm==0.31",
        "--no-cache",
    ]
    assert set(args[6:]) == {
        "--with",
        "llm-gemini",
        "llm-llama-cpp",
        "llm-templates-github",
    }
    assert llm_uv_tool.get_installed_uv_tool_packages() == [
        "llm-templates-github",
        "llm-gemini",
        "llm-llama-cpp",
    ]


def test_uninstall_rebuilds_tool_with_current_prerelease_llm(monkeypatch, tmp_path):
    calls = []
    (tmp_path / "uv-tool-packages.json").write_text(
        '["llm-llama-cpp", "llm-templates-github"]'
    )

    monkeypatch.setattr(llm_uv_tool, "user_dir", lambda: tmp_path)
    monkeypatch.setattr(llm_uv_tool, "version", lambda package: "0.32a2")
    monkeypatch.setattr(llm_uv_tool, "get_plugins", lambda: [])
    monkeypatch.setattr(
        llm_uv_tool.subprocess,
        "run",
        lambda args, check: calls.append((args, check)),
    )

    result = CliRunner().invoke(cli(), ["uninstall", "-y", "llm-llama-cpp"])

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
                "llm-templates-github",
            ],
            True,
        )
    ]
    assert llm_uv_tool.get_installed_uv_tool_packages() == ["llm-templates-github"]
