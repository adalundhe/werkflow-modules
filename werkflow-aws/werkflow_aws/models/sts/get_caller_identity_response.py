from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GetCallerIdentityResponse(BaseModel):
    UserId: StrictStr | None = None
    Account: StrictStr | None = None
    Arn: StrictStr | None = None
