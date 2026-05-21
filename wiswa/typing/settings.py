"""Shared type aliases used by both ``wiswa`` and ``wiswa-vcs``."""
from __future__ import annotations

from typing import Literal, TypeAlias

__all__ = ('PackageManager', 'ProjectType')

PackageManager: TypeAlias = Literal['poetry', 'uv']
"""
The Python package manager to use.

:meta hide-value:
"""
ProjectType: TypeAlias = Literal['c', 'c++', 'generic', 'lua', 'python', 'typescript', 'xcode']
"""
The type of project being generated.

:meta hide-value:
"""
