from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_thing_connectivity import IoTThingConnectivity


class IoTThingDocument(BaseModel):
    thingName: StrictStr | None = None
    thingId: StrictStr | None = None
    thingTypeName: StrictStr | None = None
    thingGroupNames: list[StrictStr] | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    shadow: StrictStr | None = None
    deviceDefender: StrictStr | None = None
    connectivity: IoTThingConnectivity | None = None
