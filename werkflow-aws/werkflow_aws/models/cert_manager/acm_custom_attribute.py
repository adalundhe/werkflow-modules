from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ACMCustomAttribute(BaseModel):
    ObjectIdentifier: StrictStr | None = None
    Value: StrictStr | None = None
