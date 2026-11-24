from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPRecoveryOptionType(BaseModel):
    Priority: StrictInt | None = None
    Name: StrictStr | None = None
