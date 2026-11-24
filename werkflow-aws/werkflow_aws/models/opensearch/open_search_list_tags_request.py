from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchListTagsRequest(BaseModel):
    ARN: StrictStr
