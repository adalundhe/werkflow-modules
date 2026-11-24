from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSGetAdminScopeRequest(BaseModel):
    AdminAccount: StrictStr
