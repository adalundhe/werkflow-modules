from __future__ import annotations
from pydantic import BaseModel, StrictBool


class KinesisAnalyticsApplicationSystemRollbackConfigurationUpdate(BaseModel):
    RollbackEnabledUpdate: StrictBool
