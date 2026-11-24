from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
