from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_tag import PersonalizeTag


class PersonalizeTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[PersonalizeTag]
