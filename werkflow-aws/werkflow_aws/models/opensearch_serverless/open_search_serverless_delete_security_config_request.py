from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessDeleteSecurityConfigRequest(BaseModel):
    id: StrictStr
    clientToken: StrictStr | None = None
