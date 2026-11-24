from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConfigServiceDescribeOrganizationConfigRuleStatusesRequest(BaseModel):
    OrganizationConfigRuleNames: list[StrictStr] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
