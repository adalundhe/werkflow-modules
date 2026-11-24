from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_public_tag import ECRPublicTag


class ECRPublicTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[ECRPublicTag]
