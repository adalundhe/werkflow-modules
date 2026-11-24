from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class FMSGetAdminAccountResponse(BaseModel):
    AdminAccount: StrictStr | None = None
    RoleStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
