from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightReadAuthorizationCodeGrantDetails(BaseModel):
    ClientId: StrictStr | None = None
    TokenEndpoint: StrictStr | None = None
    AuthorizationEndpoint: StrictStr | None = None
