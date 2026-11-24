from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_user_profile_details import SageMakerUserProfileDetails


class SageMakerListUserProfilesResponse(BaseModel):
    UserProfiles: list[SageMakerUserProfileDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
