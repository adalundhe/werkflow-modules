from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetPackageVersionRequest(BaseModel):
    packageName: StrictStr
    versionName: StrictStr
