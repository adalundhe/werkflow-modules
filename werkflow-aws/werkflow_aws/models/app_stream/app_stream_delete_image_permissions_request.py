from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDeleteImagePermissionsRequest(BaseModel):
    Name: StrictStr
    SharedAccountId: StrictStr
