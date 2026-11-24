from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CognitoIDPUserPoolTokenSessionConfigType(BaseModel):
    MaxPerUser: StrictInt | None = None
