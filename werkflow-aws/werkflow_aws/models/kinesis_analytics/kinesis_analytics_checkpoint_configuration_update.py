from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt


class KinesisAnalyticsCheckpointConfigurationUpdate(BaseModel):
    ConfigurationTypeUpdate: Literal['DEFAULT', 'CUSTOM'] | None = None
    CheckpointingEnabledUpdate: StrictBool | None = None
    CheckpointIntervalUpdate: StrictInt | None = None
    MinPauseBetweenCheckpointsUpdate: StrictInt | None = None
