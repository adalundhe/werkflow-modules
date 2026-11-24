from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSDeleteImportedKeyMaterialRequest(BaseModel):
    KeyId: StrictStr
    KeyMaterialId: StrictStr | None = None
