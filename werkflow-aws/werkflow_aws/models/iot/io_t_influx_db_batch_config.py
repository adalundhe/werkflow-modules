from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class IoTInfluxDBBatchConfig(BaseModel):
    maxBatchSize: StrictInt | None = None
    maxBatchOpenMs: StrictInt | None = None
    maxBatchSizeBytes: StrictInt | None = None
    batchAcrossTopics: StrictBool | None = None
