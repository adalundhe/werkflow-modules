from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_admin_scope import FMSAdminScope


class FMSGetAdminScopeResponse(BaseModel):
    AdminScope: FMSAdminScope | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
