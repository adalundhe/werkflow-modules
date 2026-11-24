from __future__ import annotations
from pydantic import BaseModel, StrictBool


class KinesisAnalyticsFlinkRunConfiguration(BaseModel):
    AllowNonRestoredState: StrictBool | None = None
