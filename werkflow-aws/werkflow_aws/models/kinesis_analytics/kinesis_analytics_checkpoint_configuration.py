from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt


class KinesisAnalyticsCheckpointConfiguration(BaseModel):
    ConfigurationType: Literal['DEFAULT', 'CUSTOM']
    CheckpointingEnabled: StrictBool | None = None
    CheckpointInterval: StrictInt | None = None
    MinPauseBetweenCheckpoints: StrictInt | None = None
