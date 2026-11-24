from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteProfileRequest(BaseModel):
    ProfileId: StrictStr
