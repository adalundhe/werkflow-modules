from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag


class IoTTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[IoTTag]
