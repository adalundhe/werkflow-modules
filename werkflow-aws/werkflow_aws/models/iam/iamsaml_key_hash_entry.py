from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMSAMLKeyHashEntry(BaseModel):
    IssuerURL: StrictStr | None = None
    KeyHashes: list[StrictStr] | None = None
