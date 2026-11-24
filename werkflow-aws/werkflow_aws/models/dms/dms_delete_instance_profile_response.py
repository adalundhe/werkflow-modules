from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_instance_profile import DMSInstanceProfile


class DMSDeleteInstanceProfileResponse(BaseModel):
    InstanceProfile: DMSInstanceProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
