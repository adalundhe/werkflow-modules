from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsSessionMetric(BaseModel):
    name: Literal['Count', 'Success', 'Failure', 'Dropped', 'Duration', 'TurnsPerConversation', 'Concurrency']
    statistic: Literal['Sum', 'Avg', 'Max']
    order: Literal['Ascending', 'Descending'] | None = None
