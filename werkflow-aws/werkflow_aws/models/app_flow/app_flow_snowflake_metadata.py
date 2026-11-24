from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSnowflakeMetadata(BaseModel):
    supportedRegions: list[StrictStr] | None = None
