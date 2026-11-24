from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystUserIdentity(BaseModel):
    userType: StrictStr | None = None
    principalId: StrictStr | None = None
    userName: StrictStr | None = None
    awsAccountId: StrictStr | None = None
