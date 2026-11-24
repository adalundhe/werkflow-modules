from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreatePackageResponse(BaseModel):
    packageName: StrictStr | None = None
    packageArn: StrictStr | None = None
    description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
