from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_user_settings import SageMakerUserSettings


class SageMakerUpdateUserProfileRequest(BaseModel):
    DomainId: StrictStr
    UserProfileName: StrictStr
    UserSettings: SageMakerUserSettings | None = None
