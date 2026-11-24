from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class IoTUpdateThingGroupResponse(BaseModel):
    version: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
