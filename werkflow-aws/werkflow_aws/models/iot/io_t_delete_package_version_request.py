from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeletePackageVersionRequest(BaseModel):
    packageName: StrictStr
    versionName: StrictStr
    clientToken: StrictStr | None = None
