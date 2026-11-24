from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
