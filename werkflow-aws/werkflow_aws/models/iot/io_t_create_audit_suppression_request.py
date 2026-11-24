from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_resource_identifier import IoTResourceIdentifier


class IoTCreateAuditSuppressionRequest(BaseModel):
    checkName: StrictStr
    resourceIdentifier: IoTResourceIdentifier
    clientRequestToken: StrictStr
    expirationDate: datetime.datetime | StrictStr | None = None
    suppressIndefinitely: StrictBool | None = None
    description: StrictStr | None = None
