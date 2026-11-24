from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMExtendedKeyUsage(BaseModel):
    Name: StrictStr | None = None
    OID: StrictStr | None = None
