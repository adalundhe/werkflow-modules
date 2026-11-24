from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISTargetAccountConfiguration(BaseModel):
    roleArn: StrictStr | None = None
    accountId: StrictStr | None = None
    description: StrictStr | None = None
