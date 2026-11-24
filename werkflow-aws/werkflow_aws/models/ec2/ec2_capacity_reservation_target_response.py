from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CapacityReservationTargetResponse(BaseModel):
    CapacityReservationId: StrictStr | None = None
    CapacityReservationResourceGroupArn: StrictStr | None = None
