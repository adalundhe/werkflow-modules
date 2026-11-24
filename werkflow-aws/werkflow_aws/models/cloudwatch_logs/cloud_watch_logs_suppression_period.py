from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class CloudWatchLogsSuppressionPeriod(BaseModel):
    value: StrictInt | None = None
    suppressionUnit: Literal['SECONDS', 'MINUTES', 'HOURS'] | None = None
