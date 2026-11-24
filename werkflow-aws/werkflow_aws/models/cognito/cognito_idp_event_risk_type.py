from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CognitoIDPEventRiskType(BaseModel):
    RiskDecision: StrictStr | None = None
    RiskLevel: StrictStr | None = None
    CompromisedCredentialsDetected: StrictBool | None = None
