from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .personalize_tag import PersonalizeTag


class PersonalizeCreateDatasetGroupRequest(BaseModel):
    name: StrictStr
    roleArn: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    domain: Literal['ECOMMERCE', 'VIDEO_ON_DEMAND'] | None = None
    tags: list[PersonalizeTag] | None = None
