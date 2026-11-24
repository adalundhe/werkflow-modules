from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2UsernameField(BaseModel):
    Identifier: StrictStr | None = None
