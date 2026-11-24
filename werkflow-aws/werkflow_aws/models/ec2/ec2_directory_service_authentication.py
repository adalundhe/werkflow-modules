from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DirectoryServiceAuthentication(BaseModel):
    DirectoryId: StrictStr | None = None
