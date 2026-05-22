# wiswa-typing

<!-- WISWA-GENERATED-README:START -->

[![Python versions](https://img.shields.io/pypi/pyversions/wiswa-typing.svg?color=blue&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI - Version](https://img.shields.io/pypi/v/wiswa-typing)](https://pypi.org/project/wiswa-typing/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/Tatsh/wiswa-typing)](https://github.com/Tatsh/wiswa-typing/tags)
[![License](https://img.shields.io/github/license/Tatsh/wiswa-typing)](https://github.com/Tatsh/wiswa-typing/blob/master/LICENSE.txt)
[![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Tatsh/wiswa-typing/v0.1.0/master)](https://github.com/Tatsh/wiswa-typing/compare/v0.1.0...master)
[![CodeQL](https://github.com/Tatsh/wiswa-typing/actions/workflows/codeql.yml/badge.svg)](https://github.com/Tatsh/wiswa-typing/actions/workflows/codeql.yml)
[![QA](https://github.com/Tatsh/wiswa-typing/actions/workflows/qa.yml/badge.svg)](https://github.com/Tatsh/wiswa-typing/actions/workflows/qa.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue?logo=dependabot)](https://github.com/dependabot)
[![Documentation Status](https://readthedocs.org/projects/wiswa-typing/badge/?version=latest)](https://wiswa-typing.readthedocs.org/?badge=latest)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![uv](https://img.shields.io/badge/uv-261230?logo=astral)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Downloads](https://static.pepy.tech/badge/wiswa-typing/month)](https://pepy.tech/project/wiswa-typing)
[![Stargazers](https://img.shields.io/github/stars/Tatsh/wiswa-typing?logo=github&style=flat)](https://github.com/Tatsh/wiswa-typing/stargazers)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Prettier](https://img.shields.io/badge/Prettier-black?logo=prettier)](https://prettier.io/)

[![@Tatsh](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%2F%3Factor=did%3Aplc%3Auq42idtvuccnmtl57nsucz72&query=%24.followersCount&label=Follow+%40Tatsh&logo=bluesky&style=social)](https://bsky.app/profile/Tatsh.bsky.social)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Tatsh-black?logo=buymeacoffee)](https://buymeacoffee.com/Tatsh)
[![Libera.Chat](https://img.shields.io/badge/Libera.Chat-Tatsh-black?logo=liberadotchat)](irc://irc.libera.chat/Tatsh)
[![Mastodon Follow](https://img.shields.io/mastodon/follow/109370961877277568?domain=hostux.social&style=social)](https://hostux.social/@Tatsh)
[![Patreon](https://img.shields.io/badge/Patreon-Tatsh2-F96854?logo=patreon)](https://www.patreon.com/Tatsh2)

<!-- WISWA-GENERATED-README:STOP -->

Shared type aliases used across the Wiswa ecosystem
([wiswa](https://github.com/Tatsh/wiswa), [wiswa-vcs](https://github.com/Tatsh/wiswa-vcs),
[wiswa-mcp](https://github.com/Tatsh/wiswa-mcp)).

This package ships **types only** — there is no runtime code. Its surface is intentionally
small: just the two `Literal` aliases that more than one Wiswa package needs to agree on.

## Installation

```shell
pip install wiswa-typing
```

## Usage

```python
from wiswa.typing import PackageManager, ProjectType
```

- `PackageManager`: `Literal['poetry', 'uv']`.
- `ProjectType`: `Literal['c', 'c++', 'generic', 'lua', 'python', 'typescript', 'xcode']`.

Wiswa-internal settings shapes (`Settings`, `PyProject`, `PackageJSON`, `VSCode`, etc.) live in
[wiswa](https://github.com/Tatsh/wiswa) under `wiswa.tool.typing`. GitHub and GitLab REST
payload types (`Repository`, `Badge`, `RemoteSettings`, `ProjectSettings`, etc.) live in
[wiswa-vcs](https://github.com/Tatsh/wiswa-vcs) under `wiswa.vcs.typing`.
