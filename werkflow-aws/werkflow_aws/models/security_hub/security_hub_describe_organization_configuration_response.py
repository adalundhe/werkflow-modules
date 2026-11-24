from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_organization_configuration import SecurityHubOrganizationConfiguration


class SecurityHubDescribeOrganizationConfigurationResponse(BaseModel):
    AutoEnable: StrictBool | None = None
    MemberAccountLimitReached: StrictBool | None = None
    AutoEnableStandards: StrictStr | None = None
    OrganizationConfiguration: SecurityHubOrganizationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
