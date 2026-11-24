from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IdentityStoreEmail(BaseModel):
    Value: StrictStr | None = None
    Type: StrictStr | None = None
    Primary: StrictBool | None = None
