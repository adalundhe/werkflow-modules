from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_resource_identifier import IoTResourceIdentifier


class IoTUpdateAuditSuppressionRequest(BaseModel):
    checkName: StrictStr
    resourceIdentifier: IoTResourceIdentifier
    expirationDate: datetime.datetime | StrictStr | None = None
    suppressIndefinitely: StrictBool | None = None
    description: StrictStr | None = None
