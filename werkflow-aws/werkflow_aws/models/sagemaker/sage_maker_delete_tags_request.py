from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteTagsRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
