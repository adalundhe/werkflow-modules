from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplateSpotMarketOptionsRequest(BaseModel):
    MaxPrice: StrictStr | None = None
    SpotInstanceType: Literal['one-time', 'persistent'] | None = None
    BlockDurationMinutes: StrictInt | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    InstanceInterruptionBehavior: Literal['hibernate', 'stop', 'terminate'] | None = None
