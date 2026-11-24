from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierGrantee(BaseModel):
    Type: StrictStr | None = None
    DisplayName: StrictStr | None = None
    URI: StrictStr | None = None
    ID: StrictStr | None = None
    EmailAddress: StrictStr | None = None
