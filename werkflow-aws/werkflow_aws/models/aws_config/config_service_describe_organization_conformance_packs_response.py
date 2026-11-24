from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_organization_conformance_pack import ConfigServiceOrganizationConformancePack


class ConfigServiceDescribeOrganizationConformancePacksResponse(BaseModel):
    OrganizationConformancePacks: list[ConfigServiceOrganizationConformancePack] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
