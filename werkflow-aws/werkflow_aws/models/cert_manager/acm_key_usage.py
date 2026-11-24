from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMKeyUsage(BaseModel):
    Name: StrictStr | None = None
