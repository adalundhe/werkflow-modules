from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2PhoneNumberField(BaseModel):
    Identifier: StrictStr | None = None
