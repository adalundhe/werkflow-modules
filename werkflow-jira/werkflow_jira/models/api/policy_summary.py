from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class PolicySummary(BaseModel):
    appliedProjectIds: list[StrictInt] | None = None
    id: StrictStr | None = None
    isDefault: StrictBool | None = None
    policyDescription: StrictStr | None = None
    policyName: StrictStr | None = None
    version: StrictInt | None = None
