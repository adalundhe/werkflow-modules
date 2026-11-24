from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeUserProfileRequest(BaseModel):
    DomainId: StrictStr
    UserProfileName: StrictStr
