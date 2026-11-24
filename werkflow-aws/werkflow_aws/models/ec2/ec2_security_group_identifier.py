from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SecurityGroupIdentifier(BaseModel):
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
