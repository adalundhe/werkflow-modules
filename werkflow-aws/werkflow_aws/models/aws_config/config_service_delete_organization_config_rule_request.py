from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteOrganizationConfigRuleRequest(BaseModel):
    OrganizationConfigRuleName: StrictStr
