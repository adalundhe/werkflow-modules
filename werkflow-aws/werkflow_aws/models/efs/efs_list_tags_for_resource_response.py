from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .efs_tag import EFSTag


class EFSListTagsForResourceResponse(BaseModel):
    Tags: list[EFSTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
