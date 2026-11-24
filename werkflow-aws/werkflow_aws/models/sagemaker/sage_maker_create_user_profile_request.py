from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_user_settings import SageMakerUserSettings


class SageMakerCreateUserProfileRequest(BaseModel):
    DomainId: StrictStr
    UserProfileName: StrictStr
    SingleSignOnUserIdentifier: StrictStr | None = None
    SingleSignOnUserValue: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    UserSettings: SageMakerUserSettings | None = None
