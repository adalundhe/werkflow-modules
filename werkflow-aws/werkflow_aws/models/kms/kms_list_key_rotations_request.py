from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KMSListKeyRotationsRequest(BaseModel):
    KeyId: StrictStr
    IncludeKeyMaterial: Literal['ALL_KEY_MATERIAL', 'ROTATIONS_ONLY'] | None = None
    Limit: StrictInt | None = None
    Marker: StrictStr | None = None
