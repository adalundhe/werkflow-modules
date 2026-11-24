from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_resource_tenant_metadata import SESResourceTenantMetadata


class SESListResourceTenantsResponse(BaseModel):
    ResourceTenants: list[SESResourceTenantMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
