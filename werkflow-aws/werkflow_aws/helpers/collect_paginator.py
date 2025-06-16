from typing import Any


def collect_paginator(results: list[Any]) -> list[dict[str, Any]]:
    paginated_results: list[dict[str, Any]] = []

    for page in results:
        paginated_results.append(page)

    return paginated_results