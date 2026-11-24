from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ReservationValue(BaseModel):
    HourlyPrice: StrictStr | None = None
    RemainingTotalValue: StrictStr | None = None
    RemainingUpfrontValue: StrictStr | None = None
