from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PreviewRuleConfiguration(BaseModel):
    id: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
    ruleKey: StrictStr | None = None
