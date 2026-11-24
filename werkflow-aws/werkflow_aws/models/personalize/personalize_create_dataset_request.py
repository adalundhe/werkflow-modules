from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .personalize_tag import PersonalizeTag


class PersonalizeCreateDatasetRequest(BaseModel):
    name: StrictStr
    schemaArn: StrictStr
    datasetGroupArn: StrictStr
    datasetType: StrictStr
    tags: list[PersonalizeTag] | None = None
