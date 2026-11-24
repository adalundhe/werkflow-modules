from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAutomationRulesResourceFieldsUpdateV2(BaseModel):
    Criticality: StrictStr | None = None
