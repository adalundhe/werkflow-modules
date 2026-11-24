from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_tag import ELBv2Tag


class ELBv2AddTagsRequest(BaseModel):
    ResourceArns: list[StrictStr]
    Tags: list[ELBv2Tag]
