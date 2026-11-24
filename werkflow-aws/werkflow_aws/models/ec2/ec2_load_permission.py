from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2LoadPermission(BaseModel):
    UserId: StrictStr | None = None
    Group: StrictStr | None = None
