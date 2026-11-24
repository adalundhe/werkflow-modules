from __future__ import annotations
from pydantic import BaseModel
from .fms_resource_set import FMSResourceSet
from .fms_tag import FMSTag


class FMSPutResourceSetRequest(BaseModel):
    ResourceSet: FMSResourceSet
    TagList: list[FMSTag] | None = None
