from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_tag import EFSTag


class EFSTagResourceRequest(BaseModel):
    ResourceId: StrictStr
    Tags: list[EFSTag]
