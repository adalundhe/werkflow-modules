from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_instance_profile import IAMInstanceProfile


class IAMListInstanceProfilesResponse(BaseModel):
    InstanceProfiles: list[IAMInstanceProfile] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
