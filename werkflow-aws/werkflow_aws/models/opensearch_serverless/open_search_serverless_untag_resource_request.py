from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
