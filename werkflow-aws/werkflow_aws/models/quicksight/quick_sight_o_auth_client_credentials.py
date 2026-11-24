from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightOAuthClientCredentials(BaseModel):
    ClientId: StrictStr | None = None
    ClientSecret: StrictStr | None = None
    Username: StrictStr | None = None
