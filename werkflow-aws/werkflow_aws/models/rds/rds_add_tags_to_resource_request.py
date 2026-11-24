from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_tag import RDSTag


class RDSAddTagsToResourceRequest(BaseModel):
    ResourceName: StrictStr
    Tags: list[RDSTag]
