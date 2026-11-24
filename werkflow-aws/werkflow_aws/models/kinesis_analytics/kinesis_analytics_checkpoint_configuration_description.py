from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class KinesisAnalyticsCheckpointConfigurationDescription(BaseModel):
    ConfigurationType: StrictStr | None = None
    CheckpointingEnabled: StrictBool | None = None
    CheckpointInterval: StrictInt | None = None
    MinPauseBetweenCheckpoints: StrictInt | None = None
