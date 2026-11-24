from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBasicAuthConnectionMetadata(BaseModel):
    BaseEndpoint: StrictStr
    Username: StrictStr
    Password: StrictStr
