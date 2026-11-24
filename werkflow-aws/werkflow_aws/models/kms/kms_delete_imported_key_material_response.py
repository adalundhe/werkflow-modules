from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class KMSDeleteImportedKeyMaterialResponse(BaseModel):
    KeyId: StrictStr | None = None
    KeyMaterialId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
