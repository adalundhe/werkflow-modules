from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LightsailContainerServiceECRImagePullerRoleRequest(BaseModel):
    isActive: StrictBool | None = None
