from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreatePackageVersionResponse(BaseModel):
    packageVersionArn: StrictStr | None = None
    packageName: StrictStr | None = None
    versionName: StrictStr | None = None
    description: StrictStr | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    status: StrictStr | None = None
    errorReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
