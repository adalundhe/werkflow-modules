from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetPackageRequest(BaseModel):
    packageName: StrictStr
