from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceOrganizationConfigRuleStatus(BaseModel):
    OrganizationConfigRuleName: StrictStr | None = None
    OrganizationRuleStatus: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
