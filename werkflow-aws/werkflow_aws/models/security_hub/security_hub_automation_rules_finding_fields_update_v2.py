from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAutomationRulesFindingFieldsUpdateV2(BaseModel):
    SeverityId: StrictInt | None = None
    Comment: StrictStr | None = None
    StatusId: StrictInt | None = None
