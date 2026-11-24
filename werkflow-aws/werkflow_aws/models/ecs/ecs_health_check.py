from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSHealthCheck(BaseModel):
    command: list[StrictStr] | None = None
    interval: StrictInt | None = None
    timeout: StrictInt | None = None
    retries: StrictInt | None = None
    startPeriod: StrictInt | None = None
