# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [${version}]
### Added - for new features
### Changed - for changes in existing functionality
### Deprecated - for soon-to-be removed features
### Removed - for now removed features
### Fixed - for any bug fixes
### Security - in case of vulnerabilities
[${version}]: https://github.com/joshuadavidthomas/llm-uv-tool/releases/tag/v${version}
-->

## [Unreleased]

### Changed

- Improved documentation in README.md with clearer installation instructions, usage examples, and explanations.

### Fixed

- Fixed incorrect PyPI link in README.md.

## [0.1.2]

### Fixed

- Added proper confirmation for `llm uninstall` command when `-y/--yes` flag is not provided. The underlying `uv tool` command used doesn't include this, so it needs to be provided by this tool.

## [0.1.1]

### Removed

- Removed a couple debug if checks that slipped in without notice to first release.

## [0.1.0]

### Added

- Initial release of llm-uv-tool
- Override for `llm install` command to use uv tool install
- Override for `llm uninstall` command to use uv tool uninstall
- Functions to track installed plugins in uv environment
- Support for Python 3.10, 3.11, 3.12, 3.13

### New Contributors!

- Josh Thomas <josh@joshthomas.dev> (maintainer)

[unreleased]: https://github.com/joshuadavidthomas/llm-uv-tool/compare/v0.1.2...HEAD
[0.1.0]: https://github.com/joshuadavidthomas/llm-uv-tool/releases/tag/v0.1.0
[0.1.1]: https://github.com/joshuadavidthomas/llm-uv-tool/releases/tag/v0.1.1
[0.1.2]: https://github.com/joshuadavidthomas/llm-uv-tool/releases/tag/v0.1.2
