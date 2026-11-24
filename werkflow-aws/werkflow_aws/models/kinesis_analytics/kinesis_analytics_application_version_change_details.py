from __future__ import annotations
from pydantic import BaseModel, StrictInt


class KinesisAnalyticsApplicationVersionChangeDetails(BaseModel):
    ApplicationVersionUpdatedFrom: StrictInt | None = None
    ApplicationVersionUpdatedTo: StrictInt | None = None
