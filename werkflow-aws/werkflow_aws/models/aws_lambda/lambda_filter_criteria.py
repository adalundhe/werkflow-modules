from __future__ import annotations
from pydantic import BaseModel
from .lambda_filter import LambdaFilter


class LambdaFilterCriteria(BaseModel):
    Filters: list[LambdaFilter] | None = None
