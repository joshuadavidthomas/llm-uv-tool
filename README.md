# llm-uv-tool

[![PyPI](https://img.shields.io/pypi/v/llm-uv-tool)](https://pypi.org/project/django-bird/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/llm-uv-tool)

A plugin for [LLM](https://github.com/simonw/llm) that provides integration when installing LLM as a uv tool.

## Requirements

- Python 3.10, 3.11, 3.12, 3.13
- uv

## Installation

```bash
uv tool install --with llm-uv-tool llm
```

## Usage

This plugin overrides two built-in LLM commands:

- `llm install`
- `llm uninstall`

Once llm-uv-tool is installed as a plugin in your LLM environment, its commands will run instead of the built-in so your usage should stay the same as before.

These modified commands are wrappers around `uv tool install` with appropriate flags instead of pip, maintaining a list of installed plugins to ensure they're properly managed within uv's environment.

To install a plugin:

```bash
llm install llm-ollama
```

To uninstall a plugin:

```bash
llm uninstall llm-openrouter
```

Both llm-uv-tool commands take the same arguments as the built-in LLM commands, which map to pip's `install` and `uninstall` commands

```bash
llm install --force-reinstall llm-gpt4all
llm uninstall -y llm-gpt4all
```

The plugin maintains a list of installed packages in a JSON file located in your LLM config directory (typically `~/.config/io.datasette.llm/uv-tool-packages.json`, though the location may vary depending on your OS). This file contains a simple JSON array with an entry for each installed plugin:


```json
[
  "llm-anthropic",
  "llm-ollama",
  "llm-uv-tool"
]
```


When you install or uninstall plugins, this file is automatically updated to track your changes.

### Migrating to llm-uv-tool

If you're already using LLM with other plugins and want to migrate to using llm-uv-tool, follow these steps:

1. Install llm-uv-tool in your current LLM environment:

   ```bash
   llm install llm-uv-tool
   ```

2. Copy all installed plugins to `uv-tool-packages.json` in your LLM config directory.

   For a small number of plugins, you may want to just create this file by hand. If you would rather use jq to automate the process, this command should do the trick:

   ```bash
   llm plugins | jq "[.[].name]" > "$XDG_CONFIG_HOME/io.datasette.llm/uv-tool-packages.json"
   ```

3. To verify everything is working, you can add an additional plugin and check the contents of `uv-tool-packages.json`.

   ```bash
   llm install llm-templates-github
   ```

   After you run this command it should look something like this, with llm-templates-github at the end:

   ```json
   [
     "llm-anthropic",
     "llm-uv-tool",
     "llm-templates-github"
   ]
   ```


## Why use this?

When you install LLM as a standalone CLI tool using uv's tool feature (`uv tool install llm`), the standard plugin installation mechanism (which uses pip) doesn't play well with uv's isolated environment approach.

This plugin attempts to solve that problem by:

1. Tracking which plugins you've installed
2. Ensuring those plugins are preserved when installing/uninstalling
3. Providing a consistent installation experience that works with uv's tool system
4. Maintaining the same API and user experience as the built-in LLM install/uninstall commands

Using this plugin helps ensure your LLM plugins remain properly installed when using uv's tool system.

## License

llm-uv-tool is licensed under the MIT license. See the [`LICENSE`](LICENSE) file for more information.
