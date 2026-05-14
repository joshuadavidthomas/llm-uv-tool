from __future__ import annotations

import os
import subprocess


def run(command, env):
    return subprocess.run(
        command,
        check=True,
        capture_output=True,
        env=env,
        text=True,
    )


def test_install_preserves_prerelease_llm_version(tmp_path):
    env = os.environ.copy()
    env["UV_TOOL_DIR"] = str(tmp_path / "tools")
    env["UV_TOOL_BIN_DIR"] = str(tmp_path / "bin")

    run(
        [
            "uv",
            "tool",
            "install",
            "--python",
            "3.13",
            "--with-editable",
            ".",
            "llm==0.32a2",
        ],
        env,
    )

    llm = tmp_path / "bin" / "llm"
    assert run([llm, "--version"], env).stdout.strip() == "llm, version 0.32a2"

    run([llm, "install", "llm-templates-github"], env)

    assert run([llm, "--version"], env).stdout.strip() == "llm, version 0.32a2"
