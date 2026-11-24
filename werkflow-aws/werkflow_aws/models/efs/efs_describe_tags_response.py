from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .efs_tag import EFSTag


class EFSDescribeTagsResponse(BaseModel):
    Marker: StrictStr | None = None
    Tags: list[EFSTag] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
