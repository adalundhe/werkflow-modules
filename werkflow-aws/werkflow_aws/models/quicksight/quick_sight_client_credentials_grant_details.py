from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightClientCredentialsGrantDetails(BaseModel):
    ClientId: StrictStr
    ClientSecret: StrictStr
    TokenEndpoint: StrictStr
