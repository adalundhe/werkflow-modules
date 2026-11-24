from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_instance_profile_model import IAMInstanceProfileModel


class IAMListInstanceProfilesForRoleResponse(BaseModel):
    InstanceProfiles: list[IAMInstanceProfileModel] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
