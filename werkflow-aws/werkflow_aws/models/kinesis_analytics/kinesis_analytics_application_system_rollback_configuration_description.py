from __future__ import annotations
from pydantic import BaseModel, StrictBool


class KinesisAnalyticsApplicationSystemRollbackConfigurationDescription(BaseModel):
    RollbackEnabled: StrictBool | None = None
