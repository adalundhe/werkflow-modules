from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_tag import ECSTag


class ECSTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[ECSTag]
