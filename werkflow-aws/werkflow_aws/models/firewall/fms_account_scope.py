from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSAccountScope(BaseModel):
    Accounts: list[StrictStr] | None = None
    AllAccountsEnabled: StrictBool | None = None
    ExcludeSpecifiedAccounts: StrictBool | None = None
