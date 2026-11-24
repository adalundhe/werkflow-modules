from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_tag import PersonalizeTag


class PersonalizeCreateEventTrackerRequest(BaseModel):
    name: StrictStr
    datasetGroupArn: StrictStr
    tags: list[PersonalizeTag] | None = None
