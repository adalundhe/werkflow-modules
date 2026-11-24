from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubUnprocessedAutomationRule(BaseModel):
    RuleArn: StrictStr | None = None
    ErrorCode: StrictInt | None = None
    ErrorMessage: StrictStr | None = None
