from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_admin_scope import FMSAdminScope


class FMSPutAdminAccountRequest(BaseModel):
    AdminAccount: StrictStr
    AdminScope: FMSAdminScope | None = None
