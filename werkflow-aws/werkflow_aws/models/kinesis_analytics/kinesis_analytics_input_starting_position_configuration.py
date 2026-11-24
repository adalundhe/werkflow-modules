from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsInputStartingPositionConfiguration(BaseModel):
    InputStartingPosition: StrictStr | None = None
