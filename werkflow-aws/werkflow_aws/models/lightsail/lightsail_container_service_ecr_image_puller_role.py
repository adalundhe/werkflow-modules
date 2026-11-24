from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailContainerServiceECRImagePullerRole(BaseModel):
    isActive: StrictBool | None = None
    principalArn: StrictStr | None = None
