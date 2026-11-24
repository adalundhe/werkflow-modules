from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesImagePermission(BaseModel):
    SharedAccountId: StrictStr | None = None
