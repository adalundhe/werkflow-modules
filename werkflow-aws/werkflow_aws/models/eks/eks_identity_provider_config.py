from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSIdentityProviderConfig(BaseModel):
    type: StrictStr | None = None
    name: StrictStr | None = None
