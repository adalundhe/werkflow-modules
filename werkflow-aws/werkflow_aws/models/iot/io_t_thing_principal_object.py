from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTThingPrincipalObject(BaseModel):
    principal: StrictStr | None = None
    thingPrincipalType: StrictStr | None = None
