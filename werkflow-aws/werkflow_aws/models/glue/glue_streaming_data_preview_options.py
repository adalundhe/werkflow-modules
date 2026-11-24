from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueStreamingDataPreviewOptions(BaseModel):
    PollingTime: StrictInt | None = None
    RecordPollingLimit: StrictInt | None = None
