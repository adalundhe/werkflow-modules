from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightImageSource(BaseModel):
    PublicUrl: StrictStr | None = None
    S3Uri: StrictStr | None = None
