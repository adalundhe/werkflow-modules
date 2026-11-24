from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_member_account_status import ConfigServiceMemberAccountStatus


class ConfigServiceGetOrganizationConfigRuleDetailedStatusResponse(BaseModel):
    OrganizationConfigRuleDetailedStatus: list[ConfigServiceMemberAccountStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
