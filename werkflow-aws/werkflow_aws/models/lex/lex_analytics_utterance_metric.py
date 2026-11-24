from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LexAnalyticsUtteranceMetric(BaseModel):
    name: Literal['Count', 'Missed', 'Detected', 'UtteranceTimestamp']
    statistic: Literal['Sum', 'Avg', 'Max']
    order: Literal['Ascending', 'Descending'] | None = None
