from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraBasicAuthenticationConfiguration(BaseModel):
    Host: StrictStr | None = None
    Port: StrictInt | None = None
    Credentials: StrictStr | None = None
