from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_tenant_resource import SESTenantResource


class SESListTenantResourcesResponse(BaseModel):
    TenantResources: list[SESTenantResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
