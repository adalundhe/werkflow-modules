from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieIamUser(BaseModel):
    accountId: StrictStr | None = None
    arn: StrictStr | None = None
    principalId: StrictStr | None = None
    userName: StrictStr | None = None
