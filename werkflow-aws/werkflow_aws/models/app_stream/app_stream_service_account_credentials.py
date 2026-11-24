from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamServiceAccountCredentials(BaseModel):
    AccountName: StrictStr | None = None
    AccountPassword: StrictStr | None = None
