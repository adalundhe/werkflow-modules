from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2MoveCapacityReservationInstancesRequest(BaseModel):
    SourceCapacityReservationId: StrictStr
    DestinationCapacityReservationId: StrictStr
    InstanceCount: StrictInt
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
