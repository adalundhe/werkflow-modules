from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_watch_tag_model import CloudWatchTagModel


class CloudWatchManagedRule(BaseModel):
    TemplateName: StrictStr
    ResourceARN: StrictStr
    Tags: list[CloudWatchTagModel] | None = None
