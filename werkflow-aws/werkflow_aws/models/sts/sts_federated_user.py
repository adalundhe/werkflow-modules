from __future__ import annotations
from pydantic import BaseModel, StrictStr


class STSFederatedUser(BaseModel):
    FederatedUserId: StrictStr | None = None
    Arn: StrictStr | None = None
