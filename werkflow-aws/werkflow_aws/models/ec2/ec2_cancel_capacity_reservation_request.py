from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelCapacityReservationRequest(BaseModel):
    CapacityReservationId: StrictStr
    DryRun: StrictBool | None = None
    ApplyCancellationCharges: Literal['commitment-wind-down'] | None = None
    QuoteId: StrictStr | None = None
