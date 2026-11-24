from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag


class IoTCreateDimensionRequest(BaseModel):
    name: StrictStr
    type: Literal['TOPIC_FILTER']
    stringValues: list[StrictStr]
    clientRequestToken: StrictStr
    tags: list[IoTTag] | None = None
