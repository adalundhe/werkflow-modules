from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteUserProfileRequest(BaseModel):
    DomainId: StrictStr
    UserProfileName: StrictStr
