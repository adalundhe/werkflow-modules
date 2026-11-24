from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .sage_maker_filter import SageMakerFilter
from .sage_maker_nested_filters import SageMakerNestedFilters


class SageMakerSearchExpression(BaseModel):
    Filters: list[SageMakerFilter] | None = None
    NestedFilters: list[SageMakerNestedFilters] | None = None
    SubExpressions: list[SageMakerSearchExpression] | None = None
    Operator: Literal['And', 'Or'] | None = None
