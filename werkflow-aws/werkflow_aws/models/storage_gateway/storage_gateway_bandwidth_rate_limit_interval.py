from __future__ import annotations
from pydantic import BaseModel, StrictInt


class StorageGatewayBandwidthRateLimitInterval(BaseModel):
    StartHourOfDay: StrictInt | None = None
    StartMinuteOfHour: StrictInt | None = None
    EndHourOfDay: StrictInt | None = None
    EndMinuteOfHour: StrictInt | None = None
    DaysOfWeek: list[StrictInt] | None = None
    AverageUploadRateLimitInBitsPerSec: StrictInt | None = None
    AverageDownloadRateLimitInBitsPerSec: StrictInt | None = None
