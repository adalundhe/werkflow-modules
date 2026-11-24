from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2Cipher(BaseModel):
    Name: StrictStr | None = None
    Priority: StrictInt | None = None
