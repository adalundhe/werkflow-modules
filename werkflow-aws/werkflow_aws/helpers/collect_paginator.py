from typing import Any


def collect_paginator(
    results: list[Any],
    model: type[Any]
):
    paginated_results: list[Any] = []

    for page in results:
        results.append(
            model(
                **page['Contents']
            )
        )

    return paginated_results