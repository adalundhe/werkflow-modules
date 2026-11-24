from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSCapacityReservationRequest(BaseModel):
    reservationGroupArn: StrictStr | None = None
    reservationPreference: StrictStr | None = None
