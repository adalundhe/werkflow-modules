from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPAcrLevelConfigType(BaseModel):
    AcrValue: StrictStr | None = None
