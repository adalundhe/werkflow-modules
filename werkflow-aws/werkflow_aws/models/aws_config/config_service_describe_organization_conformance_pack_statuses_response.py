from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_organization_conformance_pack_status import ConfigServiceOrganizationConformancePackStatus


class ConfigServiceDescribeOrganizationConformancePackStatusesResponse(BaseModel):
    OrganizationConformancePackStatuses: list[ConfigServiceOrganizationConformancePackStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
