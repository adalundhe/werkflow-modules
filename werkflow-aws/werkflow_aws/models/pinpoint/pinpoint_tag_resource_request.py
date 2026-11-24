from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_tags_model import PinpointTagsModel


class PinpointTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagsModel: PinpointTagsModel
