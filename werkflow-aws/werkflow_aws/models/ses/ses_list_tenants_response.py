from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_tenant_info import SESTenantInfo


class SESListTenantsResponse(BaseModel):
    Tenants: list[SESTenantInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
