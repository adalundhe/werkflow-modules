from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSAdminAccountSummary(BaseModel):
    AdminAccount: StrictStr | None = None
    DefaultAdmin: StrictBool | None = None
    Status: StrictStr | None = None
