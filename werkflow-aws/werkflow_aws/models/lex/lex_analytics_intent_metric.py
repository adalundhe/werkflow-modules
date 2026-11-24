from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsIntentMetric(BaseModel):
    name: Literal['Count', 'Success', 'Failure', 'Switched', 'Dropped']
    statistic: Literal['Sum', 'Avg', 'Max']
    order: Literal['Ascending', 'Descending'] | None = None
