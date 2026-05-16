"""Type definitions for the subset of GitHub REST payloads consumed by the Wiswa ecosystem."""
from __future__ import annotations

from typing import Literal, TypedDict

__all__ = ('Repository', 'RepositoryLicense', 'RepositoryOwner')


class RepositoryOwner(TypedDict, total=False):
    """Subset of the GitHub *simple-user* object embedded in a repository response."""

    avatar_url: str
    """Avatar image URL."""
    html_url: str
    """Public profile URL."""
    id: int
    """Account identifier."""
    login: str
    """Account login name."""
    node_id: str
    """Opaque GraphQL node identifier."""
    site_admin: bool
    """Whether the account is a GitHub staff member."""
    type: Literal['User', 'Organization', 'Bot']
    """Account kind."""
    url: str
    """API resource URL for the account."""


class RepositoryLicense(TypedDict, total=False):
    """Subset of the GitHub *nullable-license-simple* object embedded in a repository response."""

    key: str
    """SPDX-style license identifier (for example ``mit``)."""
    name: str
    """Human-readable license name."""
    node_id: str
    """Opaque GraphQL node identifier."""
    spdx_id: str
    """SPDX license identifier (for example ``MIT``)."""
    url: str | None
    """API resource URL for the license, or ``None`` when GitHub does not host one."""


class Repository(TypedDict, total=False):
    """
    Subset of a ``GET /repos/{owner}/{repo}`` JSON body.

    Lists the identification, metadata, counts, and feature toggles that callers most
    commonly need. GitHub returns many additional fields that are intentionally omitted to
    keep this surface manageable.
    """

    allow_forking: bool
    """Whether forks of the repository are allowed."""
    archived: bool
    """Whether the repository is archived and therefore read-only."""
    created_at: str
    """ISO-8601 timestamp at which the repository was created."""
    default_branch: str
    """Name of the repository's default branch."""
    description: str | None
    """Short repository description."""
    disabled: bool
    """Whether the repository has been administratively disabled."""
    fork: bool
    """Whether the repository itself is a fork of another."""
    forks_count: int
    """Total number of forks."""
    full_name: str
    """Repository slug in ``owner/repo`` form."""
    has_discussions: bool
    """Whether GitHub Discussions is enabled."""
    has_issues: bool
    """Whether the issue tracker is enabled."""
    has_pages: bool
    """Whether GitHub Pages is published."""
    has_projects: bool
    """Whether classic Projects are enabled."""
    has_wiki: bool
    """Whether the wiki is enabled."""
    homepage: str | None
    """External homepage URL displayed on the project page."""
    html_url: str
    """Public web URL of the repository."""
    id: int
    """Repository identifier."""
    is_template: bool
    """Whether the repository is published as a template."""
    language: str | None
    """Primary language as detected by GitHub Linguist."""
    license: RepositoryLicense | None
    """License metadata, or ``None`` when no license file is detected."""
    name: str
    """Repository name without the owner prefix."""
    node_id: str
    """Opaque GraphQL node identifier."""
    open_issues_count: int
    """Number of open issues."""
    owner: RepositoryOwner
    """The user or organisation that owns the repository."""
    private: bool
    """Whether the repository is private."""
    pushed_at: str
    """ISO-8601 timestamp of the most recent push."""
    size: int
    """Repository size in kilobytes."""
    stargazers_count: int
    """Total number of stars."""
    topics: list[str]
    """Repository topics shown as tags on the project page."""
    updated_at: str
    """ISO-8601 timestamp of the most recent metadata update."""
    url: str
    """API resource URL for the repository."""
    visibility: Literal['public', 'private', 'internal']
    """Repository visibility setting."""
    watchers_count: int
    """Total number of watchers."""
    web_commit_signoff_required: bool
    """Whether commits made via the web UI must include a sign-off."""
