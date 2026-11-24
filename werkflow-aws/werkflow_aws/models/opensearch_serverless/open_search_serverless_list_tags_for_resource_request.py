from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
