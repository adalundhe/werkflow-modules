from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystDeleteAccessTokenRequest(BaseModel):
    id: StrictStr
