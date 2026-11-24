from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmDeleteTestGridProjectRequest(BaseModel):
    projectArn: StrictStr
