from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchListTagsForResourceResponse(BaseModel):
    Tags: list[CloudWatchTagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
