from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateEncryptionKey(BaseModel):
    Type: StrictStr | None = None
    Id: StrictStr | None = None
