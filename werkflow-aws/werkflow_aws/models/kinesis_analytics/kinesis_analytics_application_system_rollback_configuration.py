from __future__ import annotations
from pydantic import BaseModel, StrictBool


class KinesisAnalyticsApplicationSystemRollbackConfiguration(BaseModel):
    RollbackEnabled: StrictBool
