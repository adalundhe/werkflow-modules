from __future__ import annotations
from pydantic import BaseModel
from .lambda_filter_model import LambdaFilterModel


class LambdaFilterCriteriaModel(BaseModel):
    Filters: list[LambdaFilterModel] | None = None
