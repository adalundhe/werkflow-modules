from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteUserRequest(BaseModel):
    applicationId: StrictStr
    userId: StrictStr
