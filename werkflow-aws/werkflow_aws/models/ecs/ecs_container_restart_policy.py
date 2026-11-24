from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class ECSContainerRestartPolicy(BaseModel):
    enabled: StrictBool | None = None
    ignoredExitCodes: list[StrictInt] | None = None
    restartAttemptPeriod: StrictInt | None = None
