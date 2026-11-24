from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_resource_identifier import IoTResourceIdentifier


class IoTRelatedResource(BaseModel):
    resourceType: StrictStr | None = None
    resourceIdentifier: IoTResourceIdentifier | None = None
    additionalInfo: dict[StrictStr, StrictStr] | None = None
