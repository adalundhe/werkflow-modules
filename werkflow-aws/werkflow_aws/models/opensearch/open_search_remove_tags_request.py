from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchRemoveTagsRequest(BaseModel):
    ARN: StrictStr
    TagKeys: list[StrictStr]
