from __future__ import annotations
from pydantic import BaseModel
from .rds_tag import RDSTag


class RDSListTagsForResourceResponse(BaseModel):
    TagList: list[RDSTag] | None = None
