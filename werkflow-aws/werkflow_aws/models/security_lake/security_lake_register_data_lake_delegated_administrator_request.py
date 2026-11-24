from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeRegisterDataLakeDelegatedAdministratorRequest(BaseModel):
    accountId: StrictStr
