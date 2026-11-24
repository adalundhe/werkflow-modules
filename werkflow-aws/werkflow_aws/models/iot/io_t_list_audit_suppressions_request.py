from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .io_t_resource_identifier import IoTResourceIdentifier


class IoTListAuditSuppressionsRequest(BaseModel):
    checkName: StrictStr | None = None
    resourceIdentifier: IoTResourceIdentifier | None = None
    ascendingOrder: StrictBool | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
