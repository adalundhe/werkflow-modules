from __future__ import annotations
from botocore.paginate import Paginator
from abc import ABC, abstractmethod
from typing import Literal, Any

MatchOption = Literal[
    "EQUALS",
    "ABSENT",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "CASE_SENSITIVE",
    "CASE_INSENSITIVE",
    "GREATER_THAN_OR_EQUAL",
]

Matchable = dict[
    Literal[
        'Key',
        'MatchOptions',
        'Values'
    ],
    str | MatchOption | list[str]
]


ExpressionFields = Literal[
    'And',
    'CostCategories',
    'Dimensions',
    'Or',
    'Not',
    'Tags',
]

ExpressionValues = dict[ExpressionFields, Any] | Matchable

Expression = dict[ExpressionFields, ExpressionValues]


GroupMethod = Literal[
    'DIMENSION',
    'TAG',
    'COST_CATEGORY',
]

Group = dict[GroupMethod, str]


class CostExplorerClient(ABC):

    @abstractmethod
    def get_cost_and_usage(
        self,
        TimePeriod: dict[str, str] = None,
        Granularity: Literal['DAILY', 'MONTHLY', 'HOURLY'] = 'MONTHLY',
        Metrics: list[str] = None,
        Filter: Expression | None = None,
        GroupBy: list[Group] | None = None,
        BillingViewArn: str | None = None,
        NextPageToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(
        self,
        Operation: str,
    ) -> Paginator:
        pass

    @abstractmethod
    def close(self):
        pass