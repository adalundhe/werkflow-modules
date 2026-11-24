from __future__ import annotations
from pydantic import BaseModel
from .connect_pre_evaluation_filter import ConnectPreEvaluationFilter


class ConnectPreEvaluationFilters(BaseModel):
    AndConditions: list[ConnectPreEvaluationFilter] | None = None
