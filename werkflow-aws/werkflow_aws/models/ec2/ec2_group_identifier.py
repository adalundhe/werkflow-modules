from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2GroupIdentifier(BaseModel):
    GroupName: StrictStr | None = None
    GroupId: StrictStr | None = None
