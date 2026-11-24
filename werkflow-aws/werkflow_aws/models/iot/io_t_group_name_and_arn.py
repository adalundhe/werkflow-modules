from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGroupNameAndArn(BaseModel):
    groupName: StrictStr | None = None
    groupArn: StrictStr | None = None
