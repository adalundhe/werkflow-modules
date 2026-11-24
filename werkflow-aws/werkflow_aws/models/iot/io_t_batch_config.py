from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class IoTBatchConfig(BaseModel):
    maxBatchOpenMs: StrictInt | None = None
    maxBatchSize: StrictInt | None = None
    maxBatchSizeBytes: StrictInt | None = None
    batchAcrossTopics: StrictBool | None = None
