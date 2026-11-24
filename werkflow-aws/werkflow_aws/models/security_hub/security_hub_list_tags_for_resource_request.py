from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
