from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_resource_identifier import IoTResourceIdentifier


class IoTDescribeAuditSuppressionRequest(BaseModel):
    checkName: StrictStr
    resourceIdentifier: IoTResourceIdentifier
