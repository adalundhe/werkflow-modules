from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAPIKeyConnectionMetadata(BaseModel):
    BaseEndpoint: StrictStr
    ApiKey: StrictStr
    Email: StrictStr | None = None
