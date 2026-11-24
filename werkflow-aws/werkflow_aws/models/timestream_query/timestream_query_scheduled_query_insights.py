from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class TimestreamQueryScheduledQueryInsights(BaseModel):
    Mode: Literal['ENABLED_WITH_RATE_CONTROL', 'DISABLED']
