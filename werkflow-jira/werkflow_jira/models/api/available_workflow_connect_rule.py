from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AvailableWorkflowConnectRule(BaseModel):
    addonKey: StrictStr | None = None
    createUrl: StrictStr | None = None
    description: StrictStr | None = None
    editUrl: StrictStr | None = None
    moduleKey: StrictStr | None = None
    name: StrictStr | None = None
    ruleKey: StrictStr | None = None
    ruleType: StrictStr | None = None
    viewUrl: StrictStr | None = None
