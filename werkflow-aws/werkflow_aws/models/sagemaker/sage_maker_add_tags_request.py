from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag import SageMakerTag


class SageMakerAddTagsRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[SageMakerTag]
