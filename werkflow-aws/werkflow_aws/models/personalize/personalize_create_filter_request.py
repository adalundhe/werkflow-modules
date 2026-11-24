from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_tag import PersonalizeTag


class PersonalizeCreateFilterRequest(BaseModel):
    name: StrictStr
    datasetGroupArn: StrictStr
    filterExpression: StrictStr
    tags: list[PersonalizeTag] | None = None
