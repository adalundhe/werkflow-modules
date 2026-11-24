from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPublicListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
