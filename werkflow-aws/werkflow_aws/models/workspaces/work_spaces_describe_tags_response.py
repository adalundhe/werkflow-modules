from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesDescribeTagsResponse(BaseModel):
    TagList: list[WorkSpacesTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
