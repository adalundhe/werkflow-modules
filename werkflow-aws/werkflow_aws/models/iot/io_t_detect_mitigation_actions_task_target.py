from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDetectMitigationActionsTaskTarget(BaseModel):
    violationIds: list[StrictStr] | None = None
    securityProfileName: StrictStr | None = None
    behaviorName: StrictStr | None = None
