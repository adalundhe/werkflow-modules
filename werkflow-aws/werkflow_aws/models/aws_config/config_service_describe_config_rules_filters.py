from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConfigServiceDescribeConfigRulesFilters(BaseModel):
    EvaluationMode: Literal['DETECTIVE', 'PROACTIVE'] | None = None
    RuleEvaluationVisibility: Literal['EXTERNAL', 'INTERNAL'] | None = None
