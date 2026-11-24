from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPResourceServerScopeType(BaseModel):
    ScopeName: StrictStr | None = None
    ScopeDescription: StrictStr | None = None
