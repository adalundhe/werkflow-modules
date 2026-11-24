from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAuthorizationCodeProperties(BaseModel):
    AuthorizationCode: StrictStr | None = None
    RedirectUri: StrictStr | None = None
