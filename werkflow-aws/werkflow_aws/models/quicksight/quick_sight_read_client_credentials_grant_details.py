from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightReadClientCredentialsGrantDetails(BaseModel):
    ClientId: StrictStr | None = None
    TokenEndpoint: StrictStr | None = None
