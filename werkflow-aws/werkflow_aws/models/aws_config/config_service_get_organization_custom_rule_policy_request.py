from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceGetOrganizationCustomRulePolicyRequest(BaseModel):
    OrganizationConfigRuleName: StrictStr
