#!/usr/bin/env python3
"""
Module with type-annotated function for safe dictionary value retrieval.
"""

from typing import Mapping, Any, TypeVar, Optional

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[T] = None
) -> Optional[T]:
    """
    Returns the value for a key in a dictionary,
    or a default value if absent.
    """
    return dct.get(key, default)
