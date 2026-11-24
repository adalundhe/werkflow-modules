from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_tag import DirectoryServiceTag


class DirectoryServiceListTagsForResourceResponse(BaseModel):
    Tags: list[DirectoryServiceTag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
