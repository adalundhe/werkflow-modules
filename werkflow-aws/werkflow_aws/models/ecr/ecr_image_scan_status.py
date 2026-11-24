from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRImageScanStatus(BaseModel):
    status: StrictStr | None = None
    description: StrictStr | None = None
