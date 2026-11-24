from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPIssuerConfigurationType(BaseModel):
    Type: StrictStr | None = None
