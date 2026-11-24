from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSAssociateAdminAccountRequest(BaseModel):
    AdminAccount: StrictStr
