from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesThinClientListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
