from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowOAuthProperties(BaseModel):
    tokenUrl: StrictStr | None = None
    authCodeUrl: StrictStr | None = None
    oAuthScopes: list[StrictStr] | None = None
