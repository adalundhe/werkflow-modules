from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCreatePackageRequest(BaseModel):
    packageName: StrictStr
    description: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    clientToken: StrictStr | None = None
