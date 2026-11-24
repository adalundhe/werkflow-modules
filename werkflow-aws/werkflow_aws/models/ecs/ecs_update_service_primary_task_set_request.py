from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSUpdateServicePrimaryTaskSetRequest(BaseModel):
    cluster: StrictStr
    service: StrictStr
    primaryTaskSet: StrictStr
