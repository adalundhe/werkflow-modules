from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraUserIdentityConfiguration(BaseModel):
    IdentityAttributeName: StrictStr | None = None
