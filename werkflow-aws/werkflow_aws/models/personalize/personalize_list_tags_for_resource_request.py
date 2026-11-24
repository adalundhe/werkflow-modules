from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
