from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTAuditCheckDetails(BaseModel):
    checkRunStatus: StrictStr | None = None
    checkCompliant: StrictBool | None = None
    totalResourcesCount: StrictInt | None = None
    nonCompliantResourcesCount: StrictInt | None = None
    suppressedNonCompliantResourcesCount: StrictInt | None = None
    errorCode: StrictStr | None = None
    message: StrictStr | None = None
