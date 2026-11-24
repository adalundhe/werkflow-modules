from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeletePackageRequest(BaseModel):
    packageName: StrictStr
    clientToken: StrictStr | None = None
