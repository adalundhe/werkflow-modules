from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesModifyAccountRequest(BaseModel):
    DedicatedTenancySupport: Literal['ENABLED'] | None = None
    DedicatedTenancyManagementCidrRange: StrictStr | None = None
