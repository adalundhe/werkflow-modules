from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightReadBasicAuthConnectionMetadata(BaseModel):
    BaseEndpoint: StrictStr | None = None
    Username: StrictStr | None = None
