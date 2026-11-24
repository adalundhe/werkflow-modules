from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeAccountResponse(BaseModel):
    DedicatedTenancySupport: StrictStr | None = None
    DedicatedTenancyManagementCidrRange: StrictStr | None = None
    DedicatedTenancyAccountType: StrictStr | None = None
    Message: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
