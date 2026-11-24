from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightReadAPIKeyConnectionMetadata(BaseModel):
    BaseEndpoint: StrictStr | None = None
    Email: StrictStr | None = None
