from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SecurityHubAutomationRulesMetadata(BaseModel):
    RuleArn: StrictStr | None = None
    RuleStatus: StrictStr | None = None
    RuleOrder: StrictInt | None = None
    RuleName: StrictStr | None = None
    Description: StrictStr | None = None
    IsTerminal: StrictBool | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
