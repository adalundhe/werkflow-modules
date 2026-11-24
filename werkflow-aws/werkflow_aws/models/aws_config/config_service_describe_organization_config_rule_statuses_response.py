from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_organization_config_rule_status import ConfigServiceOrganizationConfigRuleStatus


class ConfigServiceDescribeOrganizationConfigRuleStatusesResponse(BaseModel):
    OrganizationConfigRuleStatuses: list[ConfigServiceOrganizationConfigRuleStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
