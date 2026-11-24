from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_instance_profile import DMSInstanceProfile


class DMSDescribeInstanceProfilesResponse(BaseModel):
    Marker: StrictStr | None = None
    InstanceProfiles: list[DMSInstanceProfile] | None = None
    ResponseMetadata: dict[str, Any] | None = None
