from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class DeviceFarmExecutionConfiguration(BaseModel):
    jobTimeoutMinutes: StrictInt | None = None
    accountsCleanup: StrictBool | None = None
    appPackagesCleanup: StrictBool | None = None
    videoCapture: StrictBool | None = None
    skipAppResign: StrictBool | None = None
