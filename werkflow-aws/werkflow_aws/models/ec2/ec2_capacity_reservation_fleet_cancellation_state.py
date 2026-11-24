from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CapacityReservationFleetCancellationState(BaseModel):
    CurrentFleetState: StrictStr | None = None
    PreviousFleetState: StrictStr | None = None
    CapacityReservationFleetId: StrictStr | None = None
