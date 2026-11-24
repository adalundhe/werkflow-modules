from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMOtherName(BaseModel):
    ObjectIdentifier: StrictStr | None = None
    Value: StrictStr | None = None
