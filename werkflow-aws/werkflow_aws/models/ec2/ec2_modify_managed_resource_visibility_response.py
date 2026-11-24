from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_managed_resource_visibility_settings import EC2ManagedResourceVisibilitySettings


class EC2ModifyManagedResourceVisibilityResponse(BaseModel):
    Visibility: EC2ManagedResourceVisibilitySettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
