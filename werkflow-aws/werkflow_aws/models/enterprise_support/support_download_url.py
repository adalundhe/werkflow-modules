from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportDownloadUrl(BaseModel):
    url: StrictStr | None = None
    expiryDate: StrictStr | None = None
