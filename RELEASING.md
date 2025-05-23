# Releasing a New Version

When it comes time to cut a new release, follow these steps:

1. Create a new git branch off of `main` for the release.

   Prefer the convention `release-<version>`, where `<version>` is the next incremental version number (e.g. `release-v0.1.0` for version 0.1.0).

   ```shell
   git checkout -b release-v<version>
   ```

   However, the branch name is not *super* important, as long as it is not `main`.

2. Update the version number across the project using the bumpver tool. See [this section](#choosing-the-next-version-number) for more details about choosing the correct version number.

   The `pyproject.toml` in the base of the repository contains a `[tool.bumpver]` section that configures the bumpver tool to update the version number wherever it needs to be updated and to create a commit with the appropriate commit message.

   **Note**: For any of the following commands, you can add the command line flag `--dry` to preview the changes without actually making the changes.

   A `just bump` command is provided in the project's [Justfile](https://github.com/joshuadavidthomas/llm-uv-tool/blob/main/CONTRIBUTING.md#just). Alternatively, you can swap each `just bump` below with `uv run --with bumpver bumpver` -- or install bumpver into your local environment and call it directly.

   Here are the most common commands you will need to run:

   ```shell
   just bump update --patch  # for a patch release
   just bump update --minor  # for a minor release
   just bump update --major  # for a major release
   ```

   To release a tagged version, such as a beta or release candidate, you can run:

   ```shell
   just bump update --tag=beta
   # or
   just bump update --tag=rc
   ```

   Running these commands on a tagged version will increment the tag appropriately, but will not increment the version number.

   To go from a tagged release to a full release, you can run:

   ```shell
   just bump update --tag=final
   ```

3. Ensure the [CHANGELOG](https://github.com/joshuadavidthomas/llm-uv-tool/blob/main/CHANGELOG.md) is up to date. If updates are needed, add them now in the release branch.

4. Create a pull request from the release branch to `main`.

5. Once CI has passed and all the checks are green ✅, merge the pull request.

6. Draft a [new release](https://github.com/joshuadavidthomas/llm-uv-tool/releases/new) on GitHub.

   Use the version number with a leading `v` as the tag name (e.g. `v0.1.0`).

   Allow GitHub to generate the release title and release notes, using the 'Generate release notes' button above the text box. If this is a final release coming from a tagged release (or multiple tagged releases), make sure to copy the release notes from the previous tagged release(s) to the new release notes (after the release notes already generated for this final release).

   If this is a tagged release, make sure to check the 'Set as a pre-release' checkbox.

7. Once you are satisfied with the release, publish the release. As part of the publication process, GitHub Actions will automatically publish the new version of the package to PyPI.

## Choosing the Next Version Number

We try our best to adhere to [Semantic Versioning](https://semver.org/), but we do not promise to follow it perfectly (and let's be honest, this is the case with a lot of projects using SemVer).

In general, use your best judgement when choosing the next version number. If you are unsure, you can always ask for a second opinion from another contributor.

