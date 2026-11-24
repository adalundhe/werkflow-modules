from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IAMEnableOrganizationsRootSessionsResponse(BaseModel):
    OrganizationId: StrictStr | None = None
    EnabledFeatures: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
