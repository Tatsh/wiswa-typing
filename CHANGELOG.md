<!-- markdownlint-configure-file {"MD024": { "siblings_only": true } } -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.1/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-05-21

### Changed

- **Breaking:** reduced the public API of `wiswa.typing` to just the `PackageManager` and
  `ProjectType` `Literal` type aliases. Wiswa-internal settings shapes have moved to
  `wiswa.tool.typing`, and GitHub and GitLab REST payload types have moved to `wiswa.vcs.typing`.

### Removed

- **Breaking:** the `wiswa.typing.github` and `wiswa.typing.gitlab` submodules are no longer
  importable; their contents now live in `wiswa.vcs.typing`.
- **Breaking:** the following names are no longer exported from `wiswa.typing` (Wiswa-internal
  shapes now live in `wiswa.tool.typing`; GitHub and GitLab payload shapes now live in
  `wiswa.vcs.typing`):
  - `Settings`, `SettingsGitHub`, `SettingsSocial`, `SettingsSocialMastodon`,
    `SettingsSocialTextAndURI`, and `CustomProjectBadge`.
  - `PyProject`, `PyProjectProject`, `PyProjectTool`, `PyProjectToolCommitizen`,
    `PyProjectToolPoetry`, `PackageJSON`, `PackageJSONPublishConfig`, `PythonDeps`, and
    `ExportRequirements`.
  - `VSCode`, `VSCodeLaunch`, and `VSCodeLaunchConfiguration`.
  - `Repository`, `RepositoryLicense`, and `RepositoryOwner` (from the former `github` submodule).
  - `Badge`, `RemoteSettings`, `ProjectSettings`, `ProjectApprovals`, `PushRules`,
    `BranchProtectionOverrides`, `AccessLevelEntry`, and `AccessLevel` (from the former `gitlab`
    submodule).

## [0.0.1] - 2026-05-17

### Added

- Initial release providing shared `TypedDict` definitions and type aliases for the Wiswa
  ecosystem, importable as `from wiswa.typing import Settings, PyProject, PackageJSON` and
  related names.
- `wiswa.typing.settings` module exporting Wiswa settings shapes alongside `pyproject.toml` and
  `package.json` payload types (for example `Settings`, `PyProject`, `PyProjectProject`,
  `PyProjectTool`, `PyProjectToolCommitizen`, `PyProjectToolPoetry`, `PackageJSON`,
  `PackageJSONPublishConfig`, `PackageManager`, `ProjectType`, `PythonDeps`, `ExportRequirements`,
  `CustomProjectBadge`, `SettingsGitHub`, `SettingsSocial`, `SettingsSocialMastodon`,
  `SettingsSocialTextAndURI`, `VSCode`, `VSCodeLaunch`, and `VSCodeLaunchConfiguration`).
- `wiswa.typing.github` submodule with unprefixed names (for example `gh.Repository`,
  `gh.RepositoryOwner`, `gh.RepositoryLicense`) covering the subset of GitHub REST payloads
  consumed by the Wiswa ecosystem.
- `wiswa.typing.gitlab` submodule with unprefixed names (for example `gl.Badge`,
  `gl.ProjectSettings`, `gl.ProjectApprovals`, `gl.PushRules`, `gl.RemoteSettings`,
  `gl.BranchProtectionOverrides`, `gl.AccessLevelEntry`, and the `gl.AccessLevelLiteral` type
  alias) covering the subset of GitLab REST payloads and badge shapes used by the Wiswa
  ecosystem.
- `py.typed` marker so downstream consumers pick up the bundled type information.

[unreleased]: https://github.com/Tatsh/wiswa-typing/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Tatsh/wiswa-typing/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/Tatsh/wiswa-typing/releases/tag/v0.0.1
