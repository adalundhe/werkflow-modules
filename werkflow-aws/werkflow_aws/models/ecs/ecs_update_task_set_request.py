from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_scale import ECSScale


class ECSUpdateTaskSetRequest(BaseModel):
    cluster: StrictStr
    service: StrictStr
    taskSet: StrictStr
    scale: ECSScale
