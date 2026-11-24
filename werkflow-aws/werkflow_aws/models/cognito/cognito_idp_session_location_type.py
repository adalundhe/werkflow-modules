from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPSessionLocationType(BaseModel):
    City: StrictStr | None = None
    Country: StrictStr | None = None
