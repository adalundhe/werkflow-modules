from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSKeyListEntry(BaseModel):
    KeyId: StrictStr | None = None
    KeyArn: StrictStr | None = None
