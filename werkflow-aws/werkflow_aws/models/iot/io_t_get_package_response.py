from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTGetPackageResponse(BaseModel):
    packageName: StrictStr | None = None
    packageArn: StrictStr | None = None
    description: StrictStr | None = None
    defaultVersionName: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
