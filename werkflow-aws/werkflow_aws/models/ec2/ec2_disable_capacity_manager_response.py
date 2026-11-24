from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableCapacityManagerResponse(BaseModel):
    CapacityManagerStatus: StrictStr | None = None
    OrganizationsAccess: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
