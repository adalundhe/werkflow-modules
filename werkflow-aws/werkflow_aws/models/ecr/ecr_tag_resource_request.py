from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_tag import ECRTag


class ECRTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[ECRTag]
