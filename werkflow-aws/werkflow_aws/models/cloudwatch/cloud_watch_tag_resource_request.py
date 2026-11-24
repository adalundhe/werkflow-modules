from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[CloudWatchTagModel]
