from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTUpdatePackageRequest(BaseModel):
    packageName: StrictStr
    description: StrictStr | None = None
    defaultVersionName: StrictStr | None = None
    unsetDefaultVersion: StrictBool | None = None
    clientToken: StrictStr | None = None
