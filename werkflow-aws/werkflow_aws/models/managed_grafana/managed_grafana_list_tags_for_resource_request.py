from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
