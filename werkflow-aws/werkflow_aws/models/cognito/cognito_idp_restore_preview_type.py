from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPRestorePreviewType(BaseModel):
    Entity: StrictStr | None = None
    CreateCount: StrictInt | None = None
    UpdateCount: StrictInt | None = None
    DeleteCount: StrictInt | None = None
