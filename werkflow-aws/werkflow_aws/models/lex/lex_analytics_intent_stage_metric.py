from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsIntentStageMetric(BaseModel):
    name: Literal['Count', 'Success', 'Failed', 'Dropped', 'Retry']
    statistic: Literal['Sum', 'Avg', 'Max']
    order: Literal['Ascending', 'Descending'] | None = None
