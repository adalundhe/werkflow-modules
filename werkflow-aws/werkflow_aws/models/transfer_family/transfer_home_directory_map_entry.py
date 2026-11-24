from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferHomeDirectoryMapEntry(BaseModel):
    Entry: StrictStr | None = None
    Target: StrictStr | None = None
    Type: StrictStr | None = None
