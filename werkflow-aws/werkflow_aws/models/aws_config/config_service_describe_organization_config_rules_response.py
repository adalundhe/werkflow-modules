from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_organization_config_rule import ConfigServiceOrganizationConfigRule


class ConfigServiceDescribeOrganizationConfigRulesResponse(BaseModel):
    OrganizationConfigRules: list[ConfigServiceOrganizationConfigRule] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
