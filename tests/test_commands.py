from __future__ import annotations

import llm_uv_tool


def test_install_args_preserve_current_llm_version():
    assert llm_uv_tool.install_args(
        "0.32a2",
        ["llm-llama-cpp"],
        upgrade=False,
        editable=None,
        force_reinstall=False,
        no_cache_dir=False,
    ) == [
        "uv",
        "tool",
        "install",
        "--force",
        "llm==0.32a2",
        "--with",
        "llm-llama-cpp",
    ]


def test_install_args_keep_install_options():
    assert llm_uv_tool.install_args(
        "0.31",
        ["llm-llama-cpp"],
        upgrade=True,
        editable=".",
        force_reinstall=True,
        no_cache_dir=True,
    ) == [
        "uv",
        "tool",
        "install",
        "--force",
        "llm==0.31",
        "--upgrade",
        "--editable",
        ".",
        "--reinstall",
        "--no-cache",
        "--with",
        "llm-llama-cpp",
    ]


def test_uninstall_args_preserve_current_llm_version():
    assert llm_uv_tool.uninstall_args("0.32a2", []) == [
        "uv",
        "tool",
        "install",
        "--force",
        "llm==0.32a2",
    ]


def test_uninstall_args_keep_remaining_packages():
    assert llm_uv_tool.uninstall_args("0.31", ["llm-templates-github"]) == [
        "uv",
        "tool",
        "install",
        "--force",
        "llm==0.31",
        "--with",
        "llm-templates-github",
    ]
