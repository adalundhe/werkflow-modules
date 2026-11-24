from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DirectoryServiceAuthenticationRequest(BaseModel):
    DirectoryId: StrictStr | None = None
