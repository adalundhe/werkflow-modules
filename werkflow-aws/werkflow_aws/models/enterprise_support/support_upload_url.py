from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SupportUploadUrl(BaseModel):
    url: StrictStr | None = None
    partIndex: StrictInt | None = None
    expiryDate: StrictStr | None = None
