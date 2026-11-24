from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IdentityStoreRole(BaseModel):
    Value: StrictStr | None = None
    Type: StrictStr | None = None
    Primary: StrictBool | None = None
