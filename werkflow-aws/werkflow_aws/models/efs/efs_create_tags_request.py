from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .efs_tag import EFSTag


class EFSCreateTagsRequest(BaseModel):
    FileSystemId: StrictStr
    Tags: list[EFSTag]
