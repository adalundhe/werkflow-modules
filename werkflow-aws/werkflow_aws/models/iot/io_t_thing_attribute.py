from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTThingAttribute(BaseModel):
    thingName: StrictStr | None = None
    thingTypeName: StrictStr | None = None
    thingArn: StrictStr | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    version: StrictInt | None = None
