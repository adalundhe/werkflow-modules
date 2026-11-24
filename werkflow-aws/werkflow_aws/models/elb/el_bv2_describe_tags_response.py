from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_tag_description import ELBv2TagDescription


class ELBv2DescribeTagsResponse(BaseModel):
    TagDescriptions: list[ELBv2TagDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
