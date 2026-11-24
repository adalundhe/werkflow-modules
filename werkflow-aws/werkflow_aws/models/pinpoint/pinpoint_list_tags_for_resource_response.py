from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_tags_model import PinpointTagsModel


class PinpointListTagsForResourceResponse(BaseModel):
    TagsModel: PinpointTagsModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
