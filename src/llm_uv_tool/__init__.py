from __future__ import annotations

import json
import subprocess

import click
from llm import get_plugins
from llm import hookimpl
from llm import user_dir


def get_installed_uv_tool_packages():
    path = user_dir() / "uv-tool-packages.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("[]\n")
    try:
        return json.loads(path.read_text())
    except json.decoder.JSONDecodeError:
        return []


def save_installed_uv_tool_package(package_name):
    packages = get_installed_uv_tool_packages()
    if package_name not in packages:
        packages.append(package_name)
        path = user_dir() / "uv-tool-packages.json"
        path.write_text(json.dumps(packages, indent=2))


def remove_installed_uv_tool_package(package_name):
    packages = get_installed_uv_tool_packages()
    if package_name in packages:
        packages.remove(package_name)
        path = user_dir() / "uv-tool-packages.json"
        path.write_text(json.dumps(packages, indent=2))


@hookimpl
def register_commands(cli):
    @cli.command()
    @click.argument("packages", nargs=-1, required=False)
    @click.option(
        "-U", "--upgrade", is_flag=True, help="Upgrade packages to latest version"
    )
    @click.option(
        "-e",
        "--editable",
        help="Install a project in editable mode from this path",
    )
    @click.option(
        "--force-reinstall",
        is_flag=True,
        help="Reinstall all packages even if they are already up-to-date",
    )
    @click.option(
        "--no-cache-dir",
        is_flag=True,
        help="Disable the cache",
    )
    def install(packages, upgrade, editable, force_reinstall, no_cache_dir):
        args = ["uv", "tool", "install", "--force", "llm"]
        if upgrade:
            args.extend(["--upgrade"])
        if editable:
            args.extend(["--editable", editable])
        if force_reinstall:
            args.extend(["--reinstall"])
        if no_cache_dir:
            args.extend(["--no-cache"])
        packages = (
            set(get_installed_uv_tool_packages())
            | set(p["name"] for p in get_plugins())
            | set(packages)
        )
        for package in packages:
            args.extend(["--with", package])

        subprocess.run(args, check=True)

        for package in packages:
            save_installed_uv_tool_package(package)

    @cli.command()
    @click.argument("packages", nargs=-1, required=True)
    @click.option("-y", "--yes", is_flag=True, help="Don't ask for confirmation")
    def uninstall(packages, yes):
        """Uninstall Python packages from the LLM environment using uv."""
        installed_packages = set(get_installed_uv_tool_packages()) | set(
            p["name"] for p in get_plugins()
        )

        if not yes:
            package_list = ", ".join(packages)
            if not click.confirm(f"Uninstall {package_list}?"):
                click.echo("Aborted!")
                return

        args: list[str] = ["uv", "tool", "install", "--force", "llm"]
        for package in installed_packages - set(packages):
            args.extend(["--with", package])

        subprocess.run(args, check=True)

        for package in packages:
            remove_installed_uv_tool_package(package)
