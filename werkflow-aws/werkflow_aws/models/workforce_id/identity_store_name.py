from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IdentityStoreName(BaseModel):
    Formatted: StrictStr | None = None
    FamilyName: StrictStr | None = None
    GivenName: StrictStr | None = None
    MiddleName: StrictStr | None = None
    HonorificPrefix: StrictStr | None = None
    HonorificSuffix: StrictStr | None = None
