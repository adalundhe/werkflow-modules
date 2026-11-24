from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_operation import LightsailOperation


class LightsailResetDistributionCacheResponse(BaseModel):
    status: StrictStr | None = None
    createTime: datetime.datetime | StrictStr | None = None
    operation: LightsailOperation | None = None
    ResponseMetadata: dict[str, Any] | None = None
