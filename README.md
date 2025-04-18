# llm-uv-tool

A plugin for [LLM](https://github.com/simonw/llm) that provides integration when installing LLM as a uv tool.

## Requirements

- Python 3.10, 3.11, 3.12, 3.13
- uv

## Installation

```bash
uv install --with llm-uv-tool llm
```

## Usage

This plugin overrides two built-in LLM commands:

- `llm install`
- `llm uninstall`

These modified commands use uv tool install with appropriate flags instead of pip, maintaining a list of installed plugins to ensure they're properly managed within uv's environment.

## Why use this?

When you install LLM as a standalone CLI tool using uv's tool feature (`uv tool install llm`), the standard plugin installation mechanism (which uses pip) doesn't play well with uv's isolated environment approach.

This plugin attempts to solve that problem by:

1. Tracking which plugins you've installed
2. Ensuring those plugins are preserved when installing/uninstalling
3. Providing a consistent installation experience that works with uv's tool system
4. Maintaining the same API and user experience as the built-in LLM install/uninstall commands

Using this plugin helps ensure your LLM plugins remain properly installed when using uv's tool system.
