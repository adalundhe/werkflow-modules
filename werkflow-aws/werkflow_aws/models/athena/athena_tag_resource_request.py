from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .athena_tag_model import AthenaTagModel


class AthenaTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[AthenaTagModel]
