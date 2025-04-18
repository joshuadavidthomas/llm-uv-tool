# llm-uv-tool

[![PyPI](https://img.shields.io/pypi/v/llm-uv-tool)](https://pypi.org/project/llm-uv-tool/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/llm-uv-tool)

A plugin for [LLM](https://github.com/simonw/llm) that enables proper plugin management when LLM is installed as a uv tool. It resolves compatibility issues between uv's isolated environment approach and LLM's plugin system.

## Requirements

- Python 3.10, 3.11, 3.12, 3.13
- uv

## Installation

Install LLM with this plugin:

```bash
uv tool install --with llm-uv-tool llm
```

If you already have LLM installed:

```bash
llm install llm-uv-tool
```

Once installed, use LLM's standard commands to manage plugins.

If you've previously installed other LLM plugins before adding llm-uv-tool, refer to the [migration guide](#migrating-to-llm-uv-tool) below for steps to preserve them.

## Usage

This plugin provides uv-compatible versions of two built-in LLM commands:

- `llm install`
- `llm uninstall`

Once installed, llm-uv-tool's commands replace the built-in versions while maintaining the same interface and arguments. Behind the scenes, they:

1. Track installed plugins in a JSON file.
2. Map appropriate arguments between LLM's commands and uv's tool system.
3. Ensure plugins remain properly installed in uv's isolated environment.

Both commands accept the same arguments as LLM's built-in versions. These arguments are either:

- Mapped to equivalent `uv tool` CLI arguments.
- Handled internally to provide the same functionality.

```bash
llm install --force-reinstall llm-gpt4all
llm uninstall -y llm-gpt4all
```

The plugin maintains a list of installed plugins in a `uv-tool-packages.json` file located in your LLM config directory (typically `~/.config/io.datasette.llm/`, though the location may vary depending on your OS). This file contains a simple JSON array with an entry for each installed plugin:

```json
[
  "llm-anthropic",
  "llm-ollama",
  "llm-uv-tool"
]
```


When you install or uninstall plugins, this file is automatically updated to track your changes.

### Migrating to llm-uv-tool

If you have already installed LLM plugins and want to migrate to using llm-uv-tool, follow these steps:

1. Install llm-uv-tool in your current LLM environment:

   ```bash
   llm install llm-uv-tool
   ```

2. Copy all installed plugins to `uv-tool-packages.json` in your LLM config directory.

   If you have a small number of plugins, you may prefer to create this file by hand. Alternatively, you can use jq to automate the process with the following command:

   ```bash
   llm plugins | jq "[.[].name]" > "$XDG_CONFIG_HOME/io.datasette.llm/uv-tool-packages.json"
   ```

3. To verify everything is working, add an additional plugin and check the contents of `uv-tool-packages.json`.

   ```bash
   llm install llm-templates-github
   ```

   After running this command, the newly installed plugin should appear at the end of the array. Using the above command with llm-templates-github as an example, it might look something like this:

   ```json
   [
     "llm-anthropic",
     "llm-uv-tool",
     "llm-templates-github"
   ]
   ```


## Why use this?

When LLM is installed as a standalone CLI tool using uv's tool feature (`uv tool install llm`), LLM's standard pip-based plugin installation mechanism conflicts with uv's isolated environments. This means actions like upgrading LLM (`uv tool upgrade llm`) removes all your installed plugins, forcing repeated reinstallation.

llm-uv-tool solves this issue by:

1. Tracking installed plugins persistently.
2. Intercepting `llm install` and `llm uninstall` commands to correctly manage plugins within the uv tool context.
3. Ensuring a consistent and familiar experience that mirrors the built-in LLM commands.

By handling the underlying uv interactions, this plugin ensures your chosen LLM plugins remain installed and functional across upgrades and other tool management operations.

## License

llm-uv-tool is licensed under the MIT license. See the [`LICENSE`](LICENSE) file for more information.
