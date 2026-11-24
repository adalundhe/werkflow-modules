from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSOIDC(BaseModel):
    issuer: StrictStr | None = None
