from __future__ import annotations

import os
import subprocess


def test_install_preserves_prerelease_llm_version(tmp_path):
    env = os.environ.copy()
    env["UV_TOOL_DIR"] = str(tmp_path / "tools")
    env["UV_TOOL_BIN_DIR"] = str(tmp_path / "bin")

    subprocess.run(
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
        check=True,
        env=env,
    )

    llm = tmp_path / "bin" / "llm"
    before = subprocess.run(
        [llm, "--version"],
        check=True,
        capture_output=True,
        env=env,
        text=True,
    )
    assert before.stdout.strip() == "llm, version 0.32a2"

    subprocess.run([llm, "install", "llm-templates-github"], check=True, env=env)

    after = subprocess.run(
        [llm, "--version"],
        check=True,
        capture_output=True,
        env=env,
        text=True,
    )
    assert after.stdout.strip() == "llm, version 0.32a2"
