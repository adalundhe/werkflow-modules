from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAdvancedSecurityAdditionalFlowsType(BaseModel):
    CustomAuthMode: StrictStr | None = None
