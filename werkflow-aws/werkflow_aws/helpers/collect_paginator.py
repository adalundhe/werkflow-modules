from collections.abc import Iterable
from typing import Any


def collect_paginator(results: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    paginated_results: list[dict[str, Any]] = []

    for page in results:
        paginated_results.append(page)

    return paginated_results
